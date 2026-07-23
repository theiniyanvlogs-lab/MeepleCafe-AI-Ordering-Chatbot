import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";
import CartPanel from "@/components/CartPanel";

export default function Home() {
  return (
    <main className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex flex-1 flex-col overflow-hidden">
        {/* Navbar */}
        <Navbar />

        {/* Main Layout */}
        <div className="flex flex-1 overflow-hidden">
          {/* Chat Section */}
          <section className="flex flex-1 overflow-hidden">
            <ChatWindow />
          </section>

          {/* Cart Panel */}
          <aside className="hidden w-96 border-l bg-white xl:block">
            <CartPanel />
          </aside>
        </div>
      </div>
    </main>
  );
}
