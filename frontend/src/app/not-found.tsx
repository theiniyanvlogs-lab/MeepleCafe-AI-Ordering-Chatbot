import Link from "next/link";
import { ChefHat, Home, Search } from "lucide-react";

export default function NotFound() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-gradient-to-br from-green-50 via-white to-green-100 px-6">
      <div className="w-full max-w-xl rounded-3xl bg-white p-10 text-center shadow-xl">
        {/* Logo */}
        <div className="mx-auto mb-6 flex h-24 w-24 items-center justify-center rounded-full bg-green-600 shadow-lg">
          <ChefHat className="h-12 w-12 text-white" />
        </div>

        {/* 404 */}
        <h1 className="text-7xl font-extrabold text-green-600">
          404
        </h1>

        <h2 className="mt-4 text-3xl font-bold text-gray-800">
          Page Not Found
        </h2>

        <p className="mt-4 leading-7 text-gray-600">
          Sorry, the page you're looking for doesn't exist,
          may have been moved, or the URL is incorrect.
        </p>

        {/* Buttons */}
        <div className="mt-10 flex flex-col justify-center gap-4 sm:flex-row">
          <Link
            href="/"
            className="flex items-center justify-center gap-2 rounded-xl bg-green-600 px-6 py-3 font-semibold text-white transition hover:bg-green-700"
          >
            <Home size={18} />
            Back to Home
          </Link>

          <Link
            href="/menu"
            className="flex items-center justify-center gap-2 rounded-xl border border-gray-300 px-6 py-3 font-semibold text-gray-700 transition hover:bg-gray-100"
          >
            <Search size={18} />
            Browse Menu
          </Link>
        </div>

        {/* Helpful Links */}
        <div className="mt-10 border-t pt-6">
          <p className="mb-4 text-sm font-semibold text-gray-500">
            You may be looking for
          </p>

          <div className="flex flex-wrap justify-center gap-3">
            <Link
              href="/"
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700 transition hover:bg-green-200"
            >
              Home
            </Link>

            <Link
              href="/menu"
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700 transition hover:bg-green-200"
            >
              Menu
            </Link>

            <Link
              href="/orders"
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700 transition hover:bg-green-200"
            >
              Orders
            </Link>

            <Link
              href="/about"
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700 transition hover:bg-green-200"
            >
              About
            </Link>

            <Link
              href="/contact"
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700 transition hover:bg-green-200"
            >
              Contact
            </Link>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-10 border-t pt-5 text-sm text-gray-500">
          © {new Date().getFullYear()} Meeple Cafe AI Ordering Chatbot
        </div>
      </div>
    </main>
  );
}
