# Rails API Gateway Controller
# Handles incoming questions and forwards them to the Python AI service
require "net/http"
require "uri"

class Api::V1::QuestionsController < ApplicationController
  # POST /api/v1/questions
  def create
    store_id = params[:store_id]
    question = params[:question]

    unless store_id.present? && question.present?
      return render json: { error: "store_id and question are required" }, status: :bad_request
    end

    begin
      response = forward_to_ai_service(store_id, question)
      render json: response, status: response[:error].present? ? :bad_request : :ok
    rescue StandardError => e
      render json: { error: "AI service unavailable", detail: e.message }, status: :service_unavailable
    end
  end

  private

  def forward_to_ai_service(store_id, question)
    uri = URI.parse(ENV.fetch("AI_SERVICE_URL", "http://127.0.0.1:8000/ask"))

    http = Net::HTTP.new(uri.host, uri.port)
    http.read_timeout = 5
    http.open_timeout = 2

    request = Net::HTTP::Post.new(uri.request_uri, { "Content-Type" => "application/json" })
    request.body = { store_id: store_id, question: question }.to_json

    response = http.request(request)
    JSON.parse(response.body, symbolize_names: true)
  end
end
