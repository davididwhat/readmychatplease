import json
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

class AuthFetch:
    def __init__(self):
        self.cfg: dict[str, str] = {}

    def load_from_json(self, json_path: str) -> Optional[dict[str, str]]:
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                auths = json.load(file)
                
                required_keys = ['CLIENT_ID', 'APP_SECRET', 'CHANNEL_NAME']
                for key in required_keys:
                    if key not in auths:
                        raise KeyError(f"Missing required key: {key}")
                
                self.cfg = {
                    'CLIENT_ID': auths['CLIENT_ID'],
                    'APP_SECRET': auths['APP_SECRET'],
                    'CHANNEL_NAME': auths['CHANNEL_NAME']
                }
                
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

    def load_from_env(self, env_path: str) -> Optional[dict[str, str]]:
        try:
            if not Path(env_path).exists():
                print(f"Warning: {env_path} file not found")
                return None

            load_dotenv(env_path)

            required_vars = ['CLIENT_ID', 'APP_SECRET', 'CHANNEL_NAME']
            
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            if missing_vars:
                raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
            self.cfg = {
                'CLIENT_ID': os.getenv('CLIENT_ID'),
                'APP_SECRET': os.getenv('APP_SECRET'),
                'CHANNEL_NAME': os.getenv('CHANNEL_NAME')
            }
            
            return self.cfg
            
        except Exception as e:
            print(f"Error loading environment variables: {e}")
            return None
        
    def load_config(self, env_path: str = ".env", json_path: str = None) -> Optional[dict[str, str]]:
        env_config = self.load_from_env(env_path)
        if env_config:
            return env_config
        
        if json_path:
            return self.load_from_json(json_path)
        
        return None
    
    def get_config(self) -> dict[str, str]:
        return self.cfg
    