"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { useCart } from "@/context/CartContext";
import { api } from "@/services/api";

export default function CheckoutPage() {
  const router = useRouter();

  const { items, total, clearCart } = useCart();

  const [customerName, setCustomerName] = useState("");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");
  const [paymentMethod, setPaymentMethod] = useState("Cash");

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  async function handleOrder() {
    if (items.length === 0) {
      setMessage("Your cart is empty.");
      return;
    }

    if (!customerName || !phone || !address) {
      setMessage("Please fill all customer details.");
      return;
    }

    try {
      setLoading(true);
      setMessage("");

      await api.placeOrder({
        customer_name: customerName,
        phone,
        address,
        payment_method: paymentMethod,
        items: items.map((item) => ({
          id: item.id,
          quantity: item.quantity,
        })),
      });

      clearCart();

      setMessage("✅ Order placed successfully!");

      setTimeout(() => {
        router.push("/");
      }, 1500);
    } catch (error) {
      console.error(error);
      setMessage("❌ Failed to place order.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-gray-100 py-10">
      <div className="mx-auto max-w-6xl px-6">
        <h1 className="mb-8 text-4xl font-bold">
          Checkout
        </h1>

        <div className="grid gap-8 lg:grid-cols-2">
          {/* Customer Details */}
          <div className="rounded-2xl bg-white p-6 shadow">
            <h2 className="mb-6 text-2xl font-semibold">
              Customer Details
            </h2>

            <div className="space-y-5">
              <div>
                <label className="mb-2 block font-medium">
                  Full Name
                </label>

                <input
                  type="text"
                  value={customerName}
                  onChange={(e) =>
                    setCustomerName(e.target.value)
                  }
                  className="w-full rounded-xl border p-3"
                  placeholder="Enter your name"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Phone Number
                </label>

                <input
                  type="tel"
                  value={phone}
                  onChange={(e) =>
                    setPhone(e.target.value)
                  }
                  className="w-full rounded-xl border p-3"
                  placeholder="9876543210"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Delivery Address
                </label>

                <textarea
                  rows={4}
                  value={address}
                  onChange={(e) =>
                    setAddress(e.target.value)
                  }
                  className="w-full rounded-xl border p-3"
                  placeholder="Enter delivery address"
                />
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Payment Method
                </label>

                <select
                  value={paymentMethod}
                  onChange={(e) =>
                    setPaymentMethod(e.target.value)
                  }
                  className="w-full rounded-xl border p-3"
                >
                  <option>Cash</option>
                  <option>UPI</option>
                  <option>Card</option>
                </select>
              </div>
            </div>
          </div>

          {/* Order Summary */}
          <div className="rounded-2xl bg-white p-6 shadow">
            <h2 className="mb-6 text-2xl font-semibold">
              Order Summary
            </h2>

            {items.length === 0 ? (
              <p className="text-gray-500">
                Your cart is empty.
              </p>
            ) : (
              <div className="space-y-4">
                {items.map((item) => (
                  <div
                    key={item.id}
                    className="flex justify-between border-b pb-3"
                  >
                    <div>
                      <h3 className="font-semibold">
                        {item.name}
                      </h3>

                      <p className="text-sm text-gray-500">
                        Qty : {item.quantity}
                      </p>
                    </div>

                    <div className="font-bold text-green-700">
                      ₹{item.price * item.quantity}
                    </div>
                  </div>
                ))}

                <div className="flex justify-between border-t pt-5 text-2xl font-bold">
                  <span>Total</span>

                  <span className="text-green-700">
                    ₹{total}
                  </span>
                </div>

                <button
                  onClick={handleOrder}
                  disabled={loading}
                  className="mt-6 w-full rounded-xl bg-green-600 py-4 text-lg font-semibold text-white transition hover:bg-green-700 disabled:bg-gray-400"
                >
                  {loading
                    ? "Placing Order..."
                    : "Place Order"}
                </button>

                {message && (
                  <div className="rounded-xl bg-gray-100 p-4 text-center">
                    {message}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}
