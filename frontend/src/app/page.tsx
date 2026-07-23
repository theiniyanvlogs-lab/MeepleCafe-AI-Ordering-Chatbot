import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

export default function Home() {
  return (
    <main className="flex h-screen bg-gray-100">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex flex-1 flex-col">

        {/* Navbar */}
        <Navbar />

        {/* Chat Area */}
        <div className="flex flex-1">

          {/* Chat Window */}
          <section className="flex flex-1 items-center justify-center bg-gray-50">

            <div className="text-center">

              <h1 className="text-4xl font-bold text-green-700">
                🍽️ Meeple Cafe AI
              </h1>

              <p className="mt-4 text-gray-600">
                Your AI Restaurant Ordering Assistant
              </p>

              <p className="mt-2 text-sm text-gray-400">
                Ask anything about our menu, offers, or place an order.
              </p>

            </div>

          </section>

          {/* Cart Panel */}
          <aside className="hidden w-80 border-l bg-white lg:block">

            <div className="p-6">

              <h2 className="mb-4 text-xl font-semibold">
                🛒 Cart
              </h2>

              <p className="text-gray-500">
                Your cart is empty.
              </p>

            </div>

          </aside>

        </div>

      </div>

    </main>
  );
}
