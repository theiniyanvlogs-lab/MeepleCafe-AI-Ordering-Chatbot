import type {
  ChatResponse,
  MenuItem,
  OrderRequest,
  RestaurantInfo,
} from "@/types/chat";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "/api";

class ApiService {
  // ==========================================
  // AI Chat
  // ==========================================

  async sendMessage(message: string): Promise<ChatResponse> {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to connect to AI server.");
    }

    return await response.json();
  }

  // ==========================================
  // Get Menu
  // ==========================================

  async getMenu(): Promise<MenuItem[]> {
    const response = await fetch(`${API_BASE_URL}/menu`);

    if (!response.ok) {
      throw new Error("Unable to fetch menu.");
    }

    return await response.json();
  }

  // ==========================================
  // Search Menu
  // ==========================================

  async searchMenu(query: string): Promise<MenuItem[]> {
    const response = await fetch(
      `${API_BASE_URL}/menu/search?q=${encodeURIComponent(query)}`
    );

    if (!response.ok) {
      throw new Error("Search failed.");
    }

    return await response.json();
  }

  // ==========================================
  // Place Order
  // ==========================================

  async placeOrder(order: OrderRequest) {
    const response = await fetch(`${API_BASE_URL}/order`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(order),
    });

    if (!response.ok) {
      throw new Error("Order submission failed.");
    }

    return await response.json();
  }

  // ==========================================
  // Restaurant Information
  // ==========================================

  async getRestaurantInfo(): Promise<RestaurantInfo> {
    const response = await fetch(`${API_BASE_URL}/restaurant`);

    if (!response.ok) {
      throw new Error("Unable to fetch restaurant information.");
    }

    return await response.json();
  }

  // ==========================================
  // Health Check (Optional)
  // ==========================================

  async healthCheck() {
    const response = await fetch(`${API_BASE_URL}/health`);

    if (!response.ok) {
      throw new Error("Backend server is unavailable.");
    }

    return await response.json();
  }
}

const api = new ApiService();

export default api;
