/**
 * File: SideNav.tsx
 * Author: Steven "Kabbe" Karbjinsky
 * Description: ...
 *
 * For more information, see: https://github.com/xKabbe/ascendify
 */
'use client';

import Link from 'next/link';
import AscendifyLogo from '@/app/shared/AscendifyLogo';
import NavLinks from '@/app/shared/NavLinks';
import {useTheme} from '@/app/ThemeContext';
// TODO: Add toggle dark mode icons
import {AccessAlarm, ThreeDRotation} from '@mui/icons-material';

export default function SideNav() {
  const {theme, toggleTheme} = useTheme();

  return (
    <div className="flex h-full flex-col px-3 py-4 md:px-2 dark:bg-gray-800">
      <Link
        className="mb-2 flex h-20 items-center justify-center rounded-md bg-blue-500 p-4 md:h-40"
        href="/"
      >
        <div className="w-32 text-white md:w-40">
          <AscendifyLogo />
        </div>
      </Link>

      <div className="flex grow flex-row justify-between space-x-2 md:flex-col md:space-x-0 md:space-y-2">
        <NavLinks />
        <div className="hidden h-auto w-full grow rounded-md bg-gray-50 dark:bg-gray-800 md:block"></div>
        <button
          onClick={toggleTheme}
          className="flex h-[48px] items-center justify-center gap-2 rounded-lg bg-blue-500 text-sm font-medium text-white transition-colors hover:bg-blue-400 md:text-base"
        >
          Toggle {theme === 'light' ? 'Dark' : 'Light'} Mode
        </button>
      </div>
    </div>
  );
}
