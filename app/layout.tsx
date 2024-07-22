import "@/app/global/global.css";
import { inter } from "@/app/global/fonts";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: {
    template: "%s | Ascendify",
    default: "Ascendify",
  },
  description: "The official Ascendify tool.",
  metadataBase: new URL("https://example.com"),
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} antialiased`}>{children}</body>
    </html>
  );
}
