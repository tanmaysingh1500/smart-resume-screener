import { UploadCloud } from "lucide-react";
import { useDropzone, type Accept } from "react-dropzone";
import { Badge } from "@/components/ui/badge";

import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import UploadedFilesList from "./UploadFilesList";

interface UploadZoneProps {
  title: string;
  description: string;

  value: File[];
  onChange: (files: File[]) => void;

  accept: Accept;

  multiple?: boolean;
  maxFiles?: number;
  maxSize?: number;

  disabled?: boolean;
}
const TEN_MB = 10 * 1024 * 1024;
export default function UploadZone({
  title,
  description,
  value,
  onChange,
  accept,
  multiple = false,
  maxFiles = 1,
  maxSize = TEN_MB,
  disabled = false,
}: UploadZoneProps) {
  const onDrop = (acceptedFiles: File[]) => {
    console.log(acceptedFiles);
    if (multiple) {
        const uniqueFiles = acceptedFiles.filter(
            file =>
                !value.some(
                    existing =>
                        existing.name === file.name &&
                        existing.size === file.size
                )
        );
        
        onChange([...value, ...uniqueFiles]);
    } else {
      onChange(acceptedFiles.slice(0, 1));
    }
  };
  const isDisabled = disabled || (!multiple && value.length >= 1);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept,
    multiple,
    maxFiles,
    maxSize,
    disabled: isDisabled
  });

  const removeFile = (index: number) => {
    onChange(value.filter((_, i) => i !== index));
  };

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>{title}</CardTitle>

          {value.length > 0 && (
            <Badge className="bg-green-100 text-green-700 hover:bg-green-100 dark:bg-green-900/30 dark:text-green-400">
              {value.length} Uploaded
            </Badge>
          )}
        </div>

        <CardDescription>{description}</CardDescription>
      </CardHeader>

      <CardContent className="space-y-6">
        <div
          {...getRootProps()}
          className={cn(
            "cursor-pointer rounded-xl border-2 border-dashed p-10 transition-all",
            "flex flex-col items-center justify-center gap-4",
            isDragActive
              ? "border-primary bg-primary/5"
              : "border-muted-foreground/30 hover:border-primary/50 hover:bg-muted/30",
            isDisabled && "cursor-not-allowed opacity-50"
          )}
        >
          <input {...getInputProps()} />

          <UploadCloud className="h-10 w-10 text-muted-foreground" />

          <div className="text-center">
            <p className="font-medium">
              {isDragActive
                ? "Drop files here..."
                : "Drag & drop files here"}
            </p>

            <p className="text-sm text-muted-foreground">
              or click to browse
            </p>
          </div>
        </div>

        <UploadedFilesList
        files={value}
        onRemove={removeFile}
    />
      </CardContent>
    </Card>
  );
}