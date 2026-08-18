import os
import json
from datetime import datetime

class ProjectService:
    @staticmethod
    def initialize_project_structure(base_path, project_name):
        """
        Creates the standardized folder structure for the project.
        """
        project_root = os.path.join(base_path, project_name)
        
        folders = [
            "source",
            "icons",
            os.path.join("installers", "inno"),
            os.path.join("installers", "nsis"),
            os.path.join("installers", "wix"),
            "metadata"
        ]
        
        paths = {}
        for folder in folders:
            full_path = os.path.join(project_root, folder)
            os.makedirs(full_path, exist_ok=True)
            paths[folder.replace(os.sep, "_")] = full_path
            
        return project_root, paths

    @staticmethod
    def save_metadata(project_root, metadata_dict):
        """
        Saves generation metadata to a JSON file.
        """
        metadata_path = os.path.join(project_root, "metadata", "generation_log.json")
        metadata_dict["timestamp"] = datetime.now().isoformat()
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata_dict, f, indent=4, ensure_ascii=False)
        
        return metadata_path
