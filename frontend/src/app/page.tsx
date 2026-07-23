import Navbar from "@/components/Navbar";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="flex items-center justify-center h-[85vh]">
        <h2 className="text-3xl font-bold text-gray-400">
          Meeple Cafe AI Ordering Chatbot
        </h2>
      </div>
    </main>
  );
}
