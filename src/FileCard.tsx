import { FileText, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

interface FileCardProps {
  file: File;
  onRemove: () => void;
}

export default function FileCard({
  file,
  onRemove,
}: FileCardProps) {
  return (
    <Card className="flex items-center justify-between p-4">

      <div className="flex items-center gap-4">

        <FileText className="h-5 w-5 text-primary" />

        <div>
          <p className="font-medium">{file.name}</p>

          <p className="text-sm text-muted-foreground">
            {(file.size / 1024 / 1024).toFixed(2)} MB
          </p>
        </div>

      </div>

      <Button
        variant="ghost"
        size="icon"
        onClick={onRemove}
      >
        <X className="h-4 w-4" />
      </Button>

    </Card>
  );
}