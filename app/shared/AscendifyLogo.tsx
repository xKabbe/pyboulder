import { GlobeAltIcon } from "@heroicons/react/24/outline";
import { lusitana } from "@/app/global/fonts";

export default function AscendifyLogo() {
  return (
    <div
      className={`${lusitana.className} flex flex-col items-center justify-center text-white`}
    >
      <GlobeAltIcon className="h-12 w-12 rotate-[15deg]" />
      <p className="text-[44px] mb-2">Ascendify</p>
    </div>
  );
}
