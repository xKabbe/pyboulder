/**
 * File: layout.tsx
 * Author: Steven "Kabbe" Karbjinsky
 * Description: ...
 *
 * For more information, see: https://github.com/xKabbe/ascendify
 */
import '@/app/global/global.css';
import {inter} from '@/app/global/fonts';
import {Metadata} from 'next';
import {ThemeProvider} from '@/app/ThemeContext';

export const metadata: Metadata = {
  title: {
    template: '%s | Ascendify',
    default: 'Ascendify',
  },
  description: 'The official Ascendify tool.',
  metadataBase: new URL('https://example.com'),
};

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="en">
      <body className={`${inter.className} antialiased`}>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}
