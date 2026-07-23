// ======================================================
// Meeple Cafe AI Ordering Chatbot
// Shared Type Definitions
// ======================================================

// ======================================================
// Message
// ======================================================

export type Sender = "user" | "bot";

export interface Message {
  id: number;
  sender: Sender;
  text: string;
  timestamp?: string;
}

// ======================================================
// Chat
// ======================================================

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  answer: string;
}

// ======================================================
// Menu
// ======================================================

export interface MenuItem {
  id: number;
  name: string;
  category: string;
  description: string;
  price: number;
  image?: string;
}

// ======================================================
// Cart
// ======================================================

export interface CartItem extends MenuItem {
  quantity: number;
}

// ======================================================
// Order
// ======================================================

export interface OrderItem {
  id: number;
  name: string;
  quantity: number;
  price: number;
}

export interface OrderRequest {
  customer_name: string;
  phone: string;
  email?: string;
  address: string;
  payment_method: string;
  items: {
    id: number;
    quantity: number;
  }[];
}

export interface OrderResponse {
  order_id: number;
  customer_name: string;
  phone?: string;
  email?: string;
  address?: string;
  payment_method: string;
  status: string;
  total: number;
  date: string;
  items: OrderItem[];
  message?: string;
}

// ======================================================
// Restaurant
// ======================================================

export interface RestaurantInfo {
  name: string;
  address: string;
  phone: string;
  email: string;
  opening_hours: string;
}

// ======================================================
// Search
// ======================================================

export interface SearchResponse {
  results: MenuItem[];
}

// ======================================================
// Generic API Response
// ======================================================

export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

// ======================================================
// Chat State
// ======================================================

export interface ChatState {
  messages: Message[];
  loading: boolean;
}

// ======================================================
// API Error
// ======================================================

export interface ApiError {
  detail: string;
}

// ======================================================
// Health Check
// ======================================================

export interface HealthResponse {
  status: string;
  version?: string;
}
