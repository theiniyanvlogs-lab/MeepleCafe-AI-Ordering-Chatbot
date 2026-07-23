"use client";

import { Minus, Plus, ShoppingCart, Trash2 } from "lucide-react";

export interface CartItem {
  id: number;
  name: string;
  price: number;
  quantity: number;
}

interface CartPanelProps {
  items: CartItem[];
  onIncrease: (id: number) => void;
  onDecrease: (id: number) => void;
  onRemove: (id: number) => void;
  onCheckout: () => void;
}

export default function CartPanel({
  items,
  onIncrease,
  onDecrease,
  onRemove,
  onCheckout,
}: CartPanelProps) {
  const total = items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <aside className="flex h-full w-full flex-col bg-white">

      {/* Header */}
      <div className="border-b p-5">
        <div className="flex items-center gap-2">
          <ShoppingCart className="text-green-600" size={24} />
          <h2 className="text-xl font-bold">
            Your Cart
          </h2>
        </div>

        <p className="mt-1 text-sm text-gray-500">
          {items.length} item{items.length !== 1 ? "s" : ""}
        </p>
      </div>

      {/* Cart Items */}
      <div className="flex-1 overflow-y-auto p-4">

        {items.length === 0 ? (
          <div className="mt-20 text-center">
            <ShoppingCart
              size={64}
              className="mx-auto text-gray-300"
            />

            <h3 className="mt-4 text-lg font-semibold text-gray-600">
              Your cart is empty
            </h3>

            <p className="mt-2 text-sm text-gray-400">
              Add delicious food from the menu.
            </p>
          </div>
        ) : (
          <div className="space-y-4">

            {items.map((item) => (
              <div
                key={item.id}
                className="rounded-xl border p-4 shadow-sm"
              >
                <div className="flex justify-between">

                  <div>

                    <h3 className="font-semibold">
                      {item.name}
                    </h3>

                    <p className="mt-1 text-green-600 font-bold">
                      ₹{item.price}
                    </p>

                  </div>

                  <button
                    onClick={() => onRemove(item.id)}
                    className="text-red-500 hover:text-red-700"
                  >
                    <Trash2 size={18} />
                  </button>

                </div>

                <div className="mt-4 flex items-center justify-between">

                  <div className="flex items-center gap-2">

                    <button
                      onClick={() => onDecrease(item.id)}
                      className="rounded-lg border p-2 hover:bg-gray-100"
                    >
                      <Minus size={16} />
                    </button>

                    <span className="w-8 text-center font-semibold">
                      {item.quantity}
                    </span>

                    <button
                      onClick={() => onIncrease(item.id)}
                      className="rounded-lg border p-2 hover:bg-gray-100"
                    >
                      <Plus size={16} />
                    </button>

                  </div>

                  <span className="font-bold">
                    ₹{item.price * item.quantity}
                  </span>

                </div>
              </div>
            ))}

          </div>
        )}

      </div>

      {/* Footer */}
      <div className="border-t p-5">

        <div className="mb-4 flex justify-between text-lg font-bold">
          <span>Total</span>
          <span className="text-green-600">
            ₹{total}
          </span>
        </div>

        <button
          disabled={items.length === 0}
          onClick={onCheckout}
          className="w-full rounded-xl bg-green-600 py-3 font-semibold text-white transition hover:bg-green-700 disabled:cursor-not-allowed disabled:bg-gray-300"
        >
          Proceed to Checkout
        </button>

      </div>

    </aside>
  );
}
