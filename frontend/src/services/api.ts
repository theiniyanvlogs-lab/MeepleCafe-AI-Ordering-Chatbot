const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  answer: string;
}

export interface MenuItem {
  id: number;
  name: string;
  category: string;
  description: string;
  price: number;
  image?: string;
}

export interface OrderItem {
  menu_id: number;
  quantity: number;
}

export interface OrderRequest {
  customer_name: string;
  phone: string;
  items: OrderItem[];
}

class ApiService {
  // ==============================
  // AI Chat
  // ==============================
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

    return response.json();
  }

  // ==============================
  // Menu
  // ==============================
  async getMenu(): Promise<MenuItem[]> {
    const response = await fetch(`${API_BASE_URL}/menu`);

    if (!response.ok) {
      throw new Error("Unable to fetch menu.");
    }

    return response.json();
  }

  // ==============================
  // Search Menu
  // ==============================
  async searchMenu(query: string): Promise<MenuItem[]> {
    const response = await fetch(
      `${API_BASE_URL}/menu/search?q=${encodeURIComponent(query)}`
    );

    if (!response.ok) {
      throw new Error("Search failed.");
    }

    return response.json();
  }

  // ==============================
  // Place Order
  // ==============================
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

    return response.json();
  }

  // ==============================
  // Restaurant Info
  // ==============================
  async getRestaurantInfo() {
    const response = await fetch(`${API_BASE_URL}/restaurant`);

    if (!response.ok) {
      throw new Error("Unable to fetch restaurant information.");
    }

    return response.json();
  }
}

const api = new ApiService();

export default api;
