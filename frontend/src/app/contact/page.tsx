"use client";

import { useState } from "react";
import {
  Clock,
  Mail,
  MapPin,
  Phone,
  Send,
} from "lucide-react";

export default function ContactPage() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    subject: "",
    message: "",
  });

  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  function handleChange(
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement
    >
  ) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  async function handleSubmit(
    e: React.FormEvent<HTMLFormElement>
  ) {
    e.preventDefault();

    setLoading(true);
    setStatus("");

    try {
      // Replace this with your FastAPI endpoint later
      // await api.sendContactMessage(form);

      await new Promise((resolve) =>
        setTimeout(resolve, 1000)
      );

      setStatus(
        "✅ Thank you! Your message has been sent successfully."
      );

      setForm({
        name: "",
        email: "",
        phone: "",
        subject: "",
        message: "",
      });
    } catch (error) {
      console.error(error);
      setStatus(
        "❌ Unable to send your message. Please try again."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-gray-100">
      {/* Hero */}
      <section className="bg-green-700 py-16 text-white">
        <div className="mx-auto max-w-6xl px-6 text-center">
          <h1 className="text-5xl font-bold">
            Contact Us
          </h1>

          <p className="mx-auto mt-6 max-w-3xl text-lg text-green-100">
            We'd love to hear from you. Have questions,
            feedback, or need assistance? Send us a
            message and our team will get back to you.
          </p>
        </div>
      </section>

      <div className="mx-auto grid max-w-6xl gap-8 px-6 py-14 lg:grid-cols-2">
        {/* Contact Form */}
        <div className="rounded-2xl bg-white p-8 shadow">
          <h2 className="mb-6 text-3xl font-bold">
            Send a Message
          </h2>

          <form
            onSubmit={handleSubmit}
            className="space-y-5"
          >
            <div>
              <label className="mb-2 block font-medium">
                Full Name
              </label>

              <input
                type="text"
                name="name"
                value={form.name}
                onChange={handleChange}
                required
                className="w-full rounded-xl border p-3 focus:border-green-600 focus:outline-none"
                placeholder="Enter your name"
              />
            </div>

            <div>
              <label className="mb-2 block font-medium">
                Email
              </label>

              <input
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                required
                className="w-full rounded-xl border p-3 focus:border-green-600 focus:outline-none"
                placeholder="Enter your email"
              />
            </div>

            <div>
              <label className="mb-2 block font-medium">
                Phone
              </label>

              <input
                type="tel"
                name="phone"
                value={form.phone}
                onChange={handleChange}
                className="w-full rounded-xl border p-3 focus:border-green-600 focus:outline-none"
                placeholder="Enter your phone number"
              />
            </div>

            <div>
              <label className="mb-2 block font-medium">
                Subject
              </label>

              <input
                type="text"
                name="subject"
                value={form.subject}
                onChange={handleChange}
                required
                className="w-full rounded-xl border p-3 focus:border-green-600 focus:outline-none"
                placeholder="Message subject"
              />
            </div>

            <div>
              <label className="mb-2 block font-medium">
                Message
              </label>

              <textarea
                name="message"
                rows={6}
                value={form.message}
                onChange={handleChange}
                required
                className="w-full rounded-xl border p-3 focus:border-green-600 focus:outline-none"
                placeholder="Write your message..."
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="flex w-full items-center justify-center gap-2 rounded-xl bg-green-600 py-3 font-semibold text-white transition hover:bg-green-700 disabled:bg-gray-400"
            >
              <Send size={18} />

              {loading
                ? "Sending..."
                : "Send Message"}
            </button>

            {status && (
              <div className="rounded-xl bg-gray-100 p-4 text-center">
                {status}
              </div>
            )}
          </form>
        </div>

        {/* Contact Information */}
        <div className="space-y-6">
          <div className="rounded-2xl bg-white p-8 shadow">
            <h2 className="mb-6 text-3xl font-bold">
              Contact Information
            </h2>

            <div className="space-y-6">
              <div className="flex gap-4">
                <MapPin className="mt-1 text-green-600" />
                <div>
                  <h3 className="font-semibold">
                    Address
                  </h3>
                  <p className="text-gray-600">
                    Meeple Cafe
                    <br />
                    Chennai,
                    Tamil Nadu,
                    India
                  </p>
                </div>
              </div>

              <div className="flex gap-4">
                <Phone className="mt-1 text-green-600" />
                <div>
                  <h3 className="font-semibold">
                    Phone
                  </h3>
                  <p className="text-gray-600">
                    +91 98765 43210
                  </p>
                </div>
              </div>

              <div className="flex gap-4">
                <Mail className="mt-1 text-green-600" />
                <div>
                  <h3 className="font-semibold">
                    Email
                  </h3>
                  <p className="text-gray-600">
                    support@meeplecafe.com
                  </p>
                </div>
              </div>

              <div className="flex gap-4">
                <Clock className="mt-1 text-green-600" />
                <div>
                  <h3 className="font-semibold">
                    Opening Hours
                  </h3>

                  <p className="text-gray-600">
                    Monday - Friday
                    <br />
                    9:00 AM - 10:00 PM
                  </p>

                  <p className="mt-2 text-gray-600">
                    Saturday - Sunday
                    <br />
                    8:00 AM - 11:00 PM
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="rounded-2xl bg-green-600 p-8 text-white shadow">
            <h2 className="mb-4 text-2xl font-bold">
              Need Immediate Help?
            </h2>

            <p className="leading-7">
              Our AI Ordering Assistant is available
              24/7 to answer menu questions, recommend
              dishes, and help you place orders quickly.
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}
