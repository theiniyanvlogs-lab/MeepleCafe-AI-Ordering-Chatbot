// ========================================
// Chat Types
// ========================================

export interface Message {
  id: number;
  sender: "user" | "bot";
  text: string;
  timestamp?: string;
}

// ========================================
// Chat API
// ========================================

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  answer: string;
}

// ========================================
// Menu Types
// ========================================

export interface MenuItem {
  id: number;
  name: string;
  category: string;
  description: string;
  price: number;
  image?: string;
}

// ========================================
// Cart Types
// ========================================

export interface CartItem {
  id: number;
  name: string;
  price: number;
  quantity: number;
  image?: string;
}

// ========================================
// Order Types
// ========================================

export interface OrderItem {
  menu_id: number;
  quantity: number;
}

export interface OrderRequest {
  customer_name: string;
  phone: string;
  email?: string;
  address?: string;
  items: OrderItem[];
}

export interface OrderResponse {
  order_id: string;
  total: number;
  status: string;
  message: string;
}

// ========================================
// Restaurant Types
// ========================================

export interface RestaurantInfo {
  name: string;
  address: string;
  phone: string;
  email: string;
  opening_hours: string;
}

// ========================================
// Generic API Response
// ========================================

export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

// ========================================
// Search
// ========================================

export interface SearchResponse {
  results: MenuItem[];
}

// ========================================
// Chat State
// ========================================

export interface ChatState {
  messages: Message[];
  loading: boolean;
}
