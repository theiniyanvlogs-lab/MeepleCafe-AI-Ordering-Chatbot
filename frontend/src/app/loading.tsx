import { ChefHat, LoaderCircle } from "lucide-react";

export default function Loading() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-gradient-to-br from-green-50 via-white to-green-100">
      <div className="text-center">
        {/* Logo */}
        <div className="mx-auto mb-6 flex h-24 w-24 items-center justify-center rounded-full bg-green-600 shadow-lg">
          <ChefHat className="h-12 w-12 text-white" />
        </div>

        {/* Spinner */}
        <LoaderCircle className="mx-auto mb-6 h-12 w-12 animate-spin text-green-600" />

        {/* Title */}
        <h1 className="text-3xl font-bold text-gray-800">
          Meeple Cafe AI
        </h1>

        {/* Subtitle */}
        <p className="mt-3 text-lg text-gray-600">
          Preparing your delicious experience...
        </p>

        {/* Loading Bar */}
        <div className="mx-auto mt-8 h-2 w-64 overflow-hidden rounded-full bg-gray-200">
          <div className="h-full w-1/2 animate-pulse rounded-full bg-green-600"></div>
        </div>

        {/* Footer */}
        <p className="mt-6 text-sm text-gray-500">
          AI Ordering Assistant • FastAPI • Next.js • RAG
        </p>
      </div>
    </main>
  );
}
