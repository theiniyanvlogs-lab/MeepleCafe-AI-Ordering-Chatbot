"use client";

import { useEffect } from "react";
import { AlertTriangle, Home, RotateCcw } from "lucide-react";
import Link from "next/link";

interface ErrorPageProps {
  error: Error & {
    digest?: string;
  };
  reset: () => void;
}

export default function ErrorPage({
  error,
  reset,
}: ErrorPageProps) {
  useEffect(() => {
    console.error("Application Error:", error);
  }, [error]);

  return (
    <main className="flex min-h-screen items-center justify-center bg-gradient-to-br from-red-50 via-white to-red-100 px-6">
      <div className="w-full max-w-lg rounded-3xl bg-white p-10 text-center shadow-xl">
        {/* Icon */}
        <div className="mx-auto mb-6 flex h-24 w-24 items-center justify-center rounded-full bg-red-100">
          <AlertTriangle className="h-12 w-12 text-red-600" />
        </div>

        {/* Heading */}
        <h1 className="text-4xl font-bold text-gray-800">
          Oops!
        </h1>

        {/* Description */}
        <p className="mt-4 text-gray-600">
          Something went wrong while processing your request.
        </p>

        <p className="mt-2 text-sm text-gray-500">
          Please try again. If the problem continues,
          contact our support team.
        </p>

        {/* Error Details (Development Only) */}
        {process.env.NODE_ENV === "development" && (
          <div className="mt-6 rounded-xl bg-gray-100 p-4 text-left">
            <p className="mb-2 text-sm font-semibold text-gray-700">
              Error Details
            </p>

            <pre className="overflow-auto text-xs text-red-600">
              {error.message}
            </pre>
          </div>
        )}

        {/* Buttons */}
        <div className="mt-8 flex flex-col gap-4 sm:flex-row sm:justify-center">
          <button
            onClick={reset}
            className="flex items-center justify-center gap-2 rounded-xl bg-green-600 px-6 py-3 font-semibold text-white transition hover:bg-green-700"
          >
            <RotateCcw size={18} />
            Try Again
          </button>

          <Link
            href="/"
            className="flex items-center justify-center gap-2 rounded-xl border border-gray-300 px-6 py-3 font-semibold text-gray-700 transition hover:bg-gray-100"
          >
            <Home size={18} />
            Back to Home
          </Link>
        </div>

        {/* Footer */}
        <div className="mt-8 border-t pt-4 text-sm text-gray-500">
          Meeple Cafe AI Ordering Chatbot
        </div>
      </div>
    </main>
  );
}
