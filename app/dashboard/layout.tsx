/**
 * File: layout.tsx
 * Author: Steven "Kabbe" Karbjinsky
 * Description: ...
 *
 * For more information, see: https://github.com/xKabbe/ascendify
 */
import SideNav from '@/app/shared/SideNav';

export default function Layout({children}: {children: React.ReactNode}) {
  return (
    <div className="flex h-screen flex-col md:flex-row md:overflow-hidden dark:bg-gray-800 dark:text-gray-200">
      <div className="w-full flex-none md:w-64">
        <SideNav />
      </div>
      <div className="flex-grow p-6 md:overflow-y-auto md:p-12">{children}</div>
    </div>
  );
}
