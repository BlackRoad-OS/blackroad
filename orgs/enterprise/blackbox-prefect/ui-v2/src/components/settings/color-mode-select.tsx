import {
	Select,
	SelectContent,
	SelectGroup,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import { useLocalStorage } from "@/hooks/use-local-storage";
import { capitalize } from "@/utils";

const COLOR_MODES = [
	"default",
	"achromatopsia",
	"deuteranopia",
	"deuteranomaly",
	"protaponia",
	"protanomaly",
	"tritanomaly",
	"tritanopia",
] as const;
type ColorMode = (typeof COLOR_MODES)[number];

const COLOR_MODE_SWATCHES: Record<ColorMode, [string, string, string]> = {
	default: ["bg-red-500", "bg-green-500", "bg-blue-500"],
	achromatopsia: ["bg-gray-400", "bg-gray-500", "bg-gray-600"],
	deuteranopia: ["bg-amber-700", "bg-amber-500", "bg-blue-500"],
	deuteranomaly: ["bg-red-400", "bg-amber-500", "bg-blue-500"],
	protaponia: ["bg-amber-600", "bg-amber-500", "bg-blue-500"],
	protanomaly: ["bg-red-300", "bg-yellow-600", "bg-blue-500"],
	tritanomaly: ["bg-red-500", "bg-green-500", "bg-blue-300"],
	tritanopia: ["bg-red-500", "bg-green-500", "bg-pink-400"],
};

export const ColorModeSelect = () => {
	const [selectedColorMode, setSelectedColorMode] = useLocalStorage<ColorMode>(
		"prefect-color-mode",
		"default",
	);
	return (
		<div className="flex flex-col gap-1">
			<label htmlFor="color-mode-select">Color Mode</label>
			<Select
				value={selectedColorMode}
				onValueChange={(colorMode: ColorMode) =>
					setSelectedColorMode(colorMode)
				}
			>
				<SelectTrigger className="w-96" id="color-mode-select">
					<SelectValue placeholder="Select a color mode" />
				</SelectTrigger>
				<SelectContent>
					<SelectGroup>
						{COLOR_MODES.map((colorMode) => (
							<SelectItem key={colorMode} value={colorMode}>
								<span className="flex items-center gap-2">
									<span className="flex gap-0.5">
										{COLOR_MODE_SWATCHES[colorMode].map((swatch, i) => (
											<span
												key={i}
												className={`inline-block h-3 w-3 rounded-full ${swatch}`}
											/>
										))}
									</span>
									{capitalize(colorMode)}
								</span>
							</SelectItem>
						))}
					</SelectGroup>
				</SelectContent>
			</Select>
		</div>
	);
};
