"use client";

import {
  Bot,
  Brain,
  Coffee,
  Globe,
  MapPin,
  Phone,
  Sparkles,
} from "lucide-react";

export default function AboutPage() {
  const features = [
    {
      icon: <Bot className="h-8 w-8 text-green-600" />,
      title: "AI Ordering Assistant",
      description:
        "Chat naturally with our AI assistant to discover menu items, ask questions, and place food orders effortlessly.",
    },
    {
      icon: <Brain className="h-8 w-8 text-green-600" />,
      title: "Smart Recommendations",
      description:
        "Receive personalized food suggestions based on your preferences and previous conversations.",
    },
    {
      icon: <Coffee className="h-8 w-8 text-green-600" />,
      title: "Fresh & Delicious",
      description:
        "Enjoy freshly prepared meals, beverages, desserts, and snacks made with quality ingredients.",
    },
    {
      icon: <Sparkles className="h-8 w-8 text-green-600" />,
      title: "Fast Ordering",
      description:
        "Browse the menu, add items to your cart, and complete checkout in just a few clicks.",
    },
  ];

  const technologies = [
    "Next.js 15",
    "React 19",
    "TypeScript",
    "Tailwind CSS",
    "FastAPI",
    "Python",
    "SQLite",
    "FAISS",
    "RAG",
    "Sentence Transformers",
    "AI Chatbot",
  ];

  return (
    <main className="min-h-screen bg-gray-100">
      {/* Hero Section */}
      <section className="bg-green-700 py-16 text-white">
        <div className="mx-auto max-w-6xl px-6 text-center">
          <h1 className="text-5xl font-bold">
            About Meeple Cafe
          </h1>

          <p className="mx-auto mt-6 max-w-3xl text-lg leading-8 text-green-100">
            Meeple Cafe combines delicious food with modern AI technology.
            Our intelligent ordering assistant helps customers discover menu
            items, receive recommendations, and place orders quickly through a
            simple conversational experience.
          </p>
        </div>
      </section>

      {/* Mission */}
      <section className="mx-auto max-w-6xl px-6 py-14">
        <div className="grid gap-8 md:grid-cols-2">
          <div className="rounded-2xl bg-white p-8 shadow">
            <h2 className="mb-4 text-3xl font-bold">
              Our Mission
            </h2>

            <p className="leading-8 text-gray-600">
              To enhance the restaurant experience by combining quality food
              with AI-powered customer service. We aim to make ordering simple,
              personalized, and available anytime.
            </p>
          </div>

          <div className="rounded-2xl bg-white p-8 shadow">
            <h2 className="mb-4 text-3xl font-bold">
              Our Vision
            </h2>

            <p className="leading-8 text-gray-600">
              To become a modern restaurant platform where customers enjoy
              intelligent recommendations, seamless ordering, and fast service
              supported by artificial intelligence.
            </p>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="mx-auto max-w-6xl px-6 pb-14">
        <h2 className="mb-10 text-center text-4xl font-bold">
          Why Choose Meeple Cafe?
        </h2>

        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-2xl bg-white p-6 shadow transition hover:-translate-y-1 hover:shadow-lg"
            >
              <div className="mb-5">
                {feature.icon}
              </div>

              <h3 className="mb-3 text-xl font-semibold">
                {feature.title}
              </h3>

              <p className="text-gray-600">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Technology */}
      <section className="bg-white py-14">
        <div className="mx-auto max-w-6xl px-6">
          <h2 className="mb-8 text-center text-4xl font-bold">
            Technology Stack
          </h2>

          <div className="flex flex-wrap justify-center gap-4">
            {technologies.map((tech) => (
              <span
                key={tech}
                className="rounded-full bg-green-100 px-5 py-2 font-medium text-green-700"
              >
                {tech}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Contact */}
      <section className="mx-auto max-w-6xl px-6 py-14">
        <div className="rounded-2xl bg-white p-8 shadow">
          <h2 className="mb-8 text-center text-4xl font-bold">
            Visit Us
          </h2>

          <div className="grid gap-8 md:grid-cols-3">
            <div className="text-center">
              <MapPin className="mx-auto mb-4 h-8 w-8 text-green-600" />
              <h3 className="mb-2 font-semibold">
                Address
              </h3>
              <p className="text-gray-600">
                Meeple Cafe
                <br />
                Chennai, Tamil Nadu
              </p>
            </div>

            <div className="text-center">
              <Phone className="mx-auto mb-4 h-8 w-8 text-green-600" />
              <h3 className="mb-2 font-semibold">
                Phone
              </h3>
              <p className="text-gray-600">
                +91 98765 43210
              </p>
            </div>

            <div className="text-center">
              <Globe className="mx-auto mb-4 h-8 w-8 text-green-600" />
              <h3 className="mb-2 font-semibold">
                Website
              </h3>
              <p className="text-gray-600">
                www.meeplecafe.com
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
