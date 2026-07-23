import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";

export default function Home() {
  return (
    <main className="flex h-screen bg-gray-100">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <Navbar />

        <div className="flex flex-1">
          {/* Chat */}
          <section className="flex-1">
            <ChatWindow />
          </section>

          {/* Cart */}
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
