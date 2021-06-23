import os
import shutil
from pathlib import Path
import patoolib
from PIL import Image
    

class ComicsToPDF:
    """Convert comics to PDF"""
    def __init__(self, source_filepath: str, dest_filepath: str):
        self.source_filepath = source_filepath
        self.dest_filepath = dest_filepath
        self.temp_directory = Path(
            f"unzipped-{source_filepath.split(os.path.sep)[-1][:-4]}")

    def convert_comics(self):
        """Manager method to
        convert comics to PDF
        """
        self.extract_archive()
        self.images_to_pdf()

    def extract_archive(self) -> None:
        """Extract comics format which
        is usually an archive to temp directory
        """
        self.temp_directory.mkdir()
        patoolib.extract_archive(self.source_filepath, outdir=self.temp_directory)
    
    def images_to_pdf(self) -> None:
        """Convert images from temp directory
        into PDF format
        """
        included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
        
        #TODO: Add checking if we unzipped folder or images

        page_files = sorted([pf for  pf in os.listdir(self.temp_directory)
                 if any(pf.endswith(ext) for ext in included_extensions)])

        page_list = []
        for page in page_files:
            page = Image.open(os.path.join(self.temp_directory, page))
            page_list.append(page)

        page_list[0].save(
            self.dest_filepath, "PDF", resolution=100.0, save_all=True, append_images=page_list[1:]
            )            
        shutil.rmtree(self.temp_directory)
