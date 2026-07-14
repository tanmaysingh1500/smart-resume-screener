import { Card } from "./components/ui/card";
import FileCard from "./FileCard";

interface UploadedFilesListProps {
  files: File[];
  onRemove: (index: number) => void;
}

export default function UploadedFilesList({
  files,
  onRemove,
}: UploadedFilesListProps) {
  return (
    <div className="space-y-3">
      {files.map((file, index) => (
        <FileCard
          key={`${file.name}-${file.size}`}
          file={file}
          onRemove={() => onRemove(index)}
        />
      ))}
    </div>
  );
}