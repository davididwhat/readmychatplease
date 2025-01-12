import json
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

class VarFetch:
    def __init__(self):
        self.cfg: dict[str, str] = {}

    def load_from_json(self, json_path: str, keys: list[str] = None) -> Optional[dict[str, str]]:
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                auths = json.load(file)
                
                required_keys = keys
                for key in required_keys:
                    if key not in auths:
                        raise KeyError(f"Missing required key: {key}")

                self.cfg = {key: auths[key] for key in keys} if keys else auths
                
                return self.cfg
            
        except FileNotFoundError:
            print(f"Error: File not found at {json_path}")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format - {e}")
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            
        return None

    def load_from_env(self, env_path: str, keys: list[str] = []) -> Optional[dict[str, str]]:
        try:
            if not Path(env_path).exists():
                print(f"Warning: {env_path} file not found")
                return None

            load_dotenv(env_path)

            keys_to_load = [key for key in keys if key not in self.cfg]
            
            missing_vars = [key for key in keys_to_load if not os.getenv(key)]
            if missing_vars:
                raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
            self.cfg.update({key: os.getenv(key) for key in keys_to_load})
            
            return self.cfg
            
        except Exception as e:
            print(f"Error loading environment variables: {e}")
            return None
        
    def load_config(self, env_path: str = ".env", json_path: str = None, keys: list[str] = None) -> Optional[dict[str, str]]:
        env_config = self.load_from_env(env_path, keys)
        if env_config:
            return env_config
        
        if json_path:
            return self.load_from_json(json_path, keys)
    
    def config(self) -> dict[str, str]:
        return self.cfg
    