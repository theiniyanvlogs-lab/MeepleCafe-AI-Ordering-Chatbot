import type {
  ChatResponse,
  MenuItem,
  OrderRequest,
  OrderResponse,
  RestaurantInfo,
} from "@/types/chat";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "/api";

class ApiService {
  // ==========================================
  // Generic Request Handler
  // ==========================================

  private async request<T>(
    endpoint: string,
    options?: RequestInit
  ): Promise<T> {
    const response = await fetch(
      `${API_BASE_URL}${endpoint}`,
      {
        headers: {
          "Content-Type": "application/json",
          ...(options?.headers || {}),
        },
        ...options,
      }
    );

    if (!response.ok) {
      let message = "Something went wrong.";

      try {
        const error = await response.json();
        message = error.detail || error.message || message;
      } catch {
        // Ignore JSON parsing errors
      }

      throw new Error(message);
    }

    return response.json();
  }

  // ==========================================
  // AI Chat
  // ==========================================

  async sendMessage(
    message: string
  ): Promise<ChatResponse> {
    return this.request<ChatResponse>("/chat", {
      method: "POST",
      body: JSON.stringify({
        message,
      }),
    });
  }

  // ==========================================
  // Get Menu
  // ==========================================

  async getMenu(): Promise<MenuItem[]> {
    return this.request<MenuItem[]>("/menu");
  }

  // ==========================================
  // Search Menu
  // ==========================================

  async searchMenu(
    query: string
  ): Promise<MenuItem[]> {
    return this.request<MenuItem[]>(
      `/menu/search?q=${encodeURIComponent(query)}`
    );
  }

  // ==========================================
  // Place Order
  // ==========================================

  async placeOrder(
    order: OrderRequest
  ): Promise<OrderResponse> {
    return this.request<OrderResponse>("/order", {
      method: "POST",
      body: JSON.stringify(order),
    });
  }

  // ==========================================
  // Get Orders
  // ==========================================

  async getOrders(): Promise<OrderResponse[]> {
    return this.request<OrderResponse[]>("/orders");
  }

  // ==========================================
  // Restaurant Information
  // ==========================================

  async getRestaurantInfo(): Promise<RestaurantInfo> {
    return this.request<RestaurantInfo>("/restaurant");
  }

  // ==========================================
  // Health Check
  // ==========================================

  async healthCheck() {
    return this.request("/health");
  }
}

export const api = new ApiService();

export default api;
