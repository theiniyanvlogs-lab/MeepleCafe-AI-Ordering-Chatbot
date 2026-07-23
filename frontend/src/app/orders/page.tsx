"use client";

import { useCallback, useEffect, useState } from "react";
import {
  Calendar,
  CreditCard,
  Package,
  RefreshCw,
  User,
} from "lucide-react";

import { api } from "@/services/api";

interface OrderItem {
  id: number;
  name: string;
  quantity: number;
  price: number;
}

interface Order {
  order_id: number;
  customer_name: string;
  date: string;
  payment_method: string;
  status: string;
  total: number;
  items: OrderItem[];
}

export default function OrdersPage() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadOrders = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const data = await api.getOrders();

      setOrders(data);
    } catch (err) {
      console.error(err);
      setError("Unable to load orders.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadOrders();
  }, [loadOrders]);

  function statusColor(status: string) {
    switch (status.toLowerCase()) {
      case "delivered":
        return "bg-green-100 text-green-700";

      case "preparing":
        return "bg-yellow-100 text-yellow-700";

      case "ready":
        return "bg-blue-100 text-blue-700";

      case "cancelled":
        return "bg-red-100 text-red-700";

      default:
        return "bg-gray-100 text-gray-700";
    }
  }

  return (
    <main className="min-h-screen bg-gray-100">
      <div className="mx-auto max-w-6xl px-6 py-10">
        {/* Header */}

        <div className="mb-10 flex items-center justify-between">
          <div>
            <h1 className="text-4xl font-bold">
              📦 My Orders
            </h1>

            <p className="mt-2 text-gray-600">
              View your recent restaurant orders.
            </p>
          </div>

          <button
            onClick={loadOrders}
            className="flex items-center gap-2 rounded-xl bg-green-600 px-5 py-3 text-white transition hover:bg-green-700"
          >
            <RefreshCw size={18} />
            Refresh
          </button>
        </div>

        {/* Loading */}

        {loading && (
          <div className="py-20 text-center">
            <p className="text-lg font-medium">
              Loading orders...
            </p>
          </div>
        )}

        {/* Error */}

        {!loading && error && (
          <div className="rounded-xl bg-red-100 p-6 text-red-700">
            {error}
          </div>
        )}

        {/* Empty */}

        {!loading &&
          !error &&
          orders.length === 0 && (
            <div className="rounded-2xl bg-white py-20 text-center shadow">
              <Package
                size={70}
                className="mx-auto text-gray-300"
              />

              <h2 className="mt-6 text-2xl font-bold">
                No Orders Yet
              </h2>

              <p className="mt-3 text-gray-500">
                Place your first order from the menu.
              </p>
            </div>
          )}

        {/* Orders */}

        {!loading &&
          !error &&
          orders.length > 0 && (
            <div className="space-y-8">
              {orders.map((order) => (
                <div
                  key={order.order_id}
                  className="rounded-2xl bg-white p-6 shadow"
                >
                  {/* Header */}

                  <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                    <div>
                      <h2 className="text-2xl font-bold">
                        Order #{order.order_id}
                      </h2>

                      <div className="mt-3 space-y-2 text-gray-600">
                        <div className="flex items-center gap-2">
                          <User size={16} />
                          {order.customer_name}
                        </div>

                        <div className="flex items-center gap-2">
                          <Calendar size={16} />
                          {order.date}
                        </div>

                        <div className="flex items-center gap-2">
                          <CreditCard size={16} />
                          {order.payment_method}
                        </div>
                      </div>
                    </div>

                    <span
                      className={`rounded-full px-4 py-2 text-sm font-semibold ${statusColor(
                        order.status
                      )}`}
                    >
                      {order.status}
                    </span>
                  </div>

                  {/* Items */}

                  <div className="space-y-3 border-t border-b py-5">
                    {order.items.map((item) => (
                      <div
                        key={item.id}
                        className="flex justify-between"
                      >
                        <div>
                          <span className="font-medium">
                            {item.name}
                          </span>

                          <span className="ml-2 text-gray-500">
                            × {item.quantity}
                          </span>
                        </div>

                        <span className="font-semibold">
                          ₹{item.price * item.quantity}
                        </span>
                      </div>
                    ))}
                  </div>

                  {/* Footer */}

                  <div className="mt-5 flex justify-between text-xl font-bold">
                    <span>Total</span>

                    <span className="text-green-700">
                      ₹{order.total}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
      </div>
    </main>
  );
}
