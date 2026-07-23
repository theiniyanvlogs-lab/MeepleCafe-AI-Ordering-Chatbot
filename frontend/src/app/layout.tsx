import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Meeple Cafe AI Ordering Chatbot",
  description:
    "AI-powered restaurant ordering assistant built with Next.js, FastAPI, FAISS and RAG.",
  keywords: [
    "Meeple Cafe",
    "AI Chatbot",
    "Restaurant",
    "Food Ordering",
    "FastAPI",
    "Next.js",
    "RAG",
    "FAISS",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-100 text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
