"use client";

import { useEffect, useMemo, useState } from "react";

import MenuCard from "@/components/MenuCard";
import { api } from "@/services/api";
import type { MenuItem } from "@/types/chat";

export default function MenuPage() {
  const [menu, setMenu] = useState<MenuItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");

  useEffect(() => {
    async function loadMenu() {
      try {
        setLoading(true);

        const data = await api.getMenu();

        setMenu(data);
      } catch (err) {
        console.error(err);
        setError("Unable to load menu.");
      } finally {
        setLoading(false);
      }
    }

    loadMenu();
  }, []);

  const categories = useMemo(() => {
    return [
      "All",
      ...new Set(menu.map((item) => item.category)),
    ];
  }, [menu]);

  const filteredMenu = useMemo(() => {
    return menu.filter((item) => {
      const matchesSearch =
        item.name.toLowerCase().includes(search.toLowerCase()) ||
        item.description
          .toLowerCase()
          .includes(search.toLowerCase());

      const matchesCategory =
        category === "All" || item.category === category;

      return matchesSearch && matchesCategory;
    });
  }, [menu, search, category]);

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="mx-auto max-w-7xl px-6 py-10">
        {/* Header */}

        <div className="mb-10">
          <h1 className="text-4xl font-bold">
            🍽 Meeple Cafe Menu
          </h1>

          <p className="mt-2 text-gray-600">
            Discover our delicious food and beverages.
          </p>
        </div>

        {/* Search & Filter */}

        <div className="mb-8 flex flex-col gap-4 md:flex-row">
          <input
            type="text"
            placeholder="Search menu..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="flex-1 rounded-xl border bg-white px-4 py-3 outline-none focus:border-green-600"
          />

          <select
            value={category}
            onChange={(e) =>
              setCategory(e.target.value)
            }
            className="rounded-xl border bg-white px-4 py-3 outline-none focus:border-green-600"
          >
            {categories.map((cat) => (
              <option
                key={cat}
                value={cat}
              >
                {cat}
              </option>
            ))}
          </select>
        </div>

        {/* Loading */}

        {loading && (
          <div className="py-20 text-center">
            <p className="text-lg">
              Loading menu...
            </p>
          </div>
        )}

        {/* Error */}

        {!loading && error && (
          <div className="rounded-xl bg-red-100 p-6 text-red-700">
            {error}
          </div>
        )}

        {/* Empty */}

        {!loading &&
          !error &&
          filteredMenu.length === 0 && (
            <div className="py-20 text-center text-gray-500">
              No menu items found.
            </div>
          )}

        {/* Menu Grid */}

        {!loading &&
          !error &&
          filteredMenu.length > 0 && (
            <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              {filteredMenu.map((item) => (
                <MenuCard
                  key={item.id}
                  item={item}
                />
              ))}
            </div>
          )}
      </div>
    </div>
  );
}
