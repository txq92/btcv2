#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Advanced Crypto Signal Detector
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, check=True):
    """Run shell command with error handling."""
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def setup_virtual_environment():
    """Create and activate virtual environment."""
    print("\n🔧 Setting up virtual environment...")
    
    # Create virtual environment
    success, stdout, stderr = run_command("python -m venv venv")
    if not success:
        print(f"❌ Failed to create virtual environment: {stderr}")
        return False
    
    # Get activation script path
    if os.name == 'nt':  # Windows
        activate_script = os.path.join("venv", "Scripts", "activate")
        pip_path = os.path.join("venv", "Scripts", "pip")
    else:  # Unix/Linux
        activate_script = os.path.join("venv", "bin", "activate")
        pip_path = os.path.join("venv", "bin", "pip")
    
    print(f"✅ Virtual environment created")
    print(f"📋 To activate manually: {activate_script}")
    
    return True

def install_dependencies():
    """Install required Python packages."""
    print("\n📦 Installing dependencies...")
    
    # Determine pip path
    if os.name == 'nt':  # Windows
        pip_cmd = os.path.join("venv", "Scripts", "pip")
    else:  # Unix/Linux
        pip_cmd = os.path.join("venv", "bin", "pip")
    
    # Install requirements
    success, stdout, stderr = run_command(f"{pip_cmd} install -r requirements.txt")
    if not success:
        print(f"❌ Failed to install dependencies: {stderr}")
        return False
    
    print("✅ Dependencies installed successfully")
    return True

def setup_configuration():
    """Setup configuration file."""
    print("\n⚙️ Setting up configuration...")
    
    config_file = Path("config.py")
    example_file = Path("config.example.py")
    
    if not config_file.exists() and example_file.exists():
        shutil.copy2(example_file, config_file)
        print("✅ Configuration template created: config.py")
        print("📝 Please edit config.py with your Telegram bot token and chat ID")
    elif config_file.exists():
        print("✅ Configuration file already exists")
    else:
        print("⚠️ No configuration template found")
    
    return True

def check_docker():
    """Check if Docker is available."""
    print("\n🐳 Checking Docker availability...")
    
    success, stdout, stderr = run_command("docker --version", check=False)
    if success:
        print(f"✅ Docker available: {stdout.strip()}")
        
        # Check docker-compose
        success2, stdout2, stderr2 = run_command("docker-compose --version", check=False)
        if success2:
            print(f"✅ Docker Compose available: {stdout2.strip()}")
            return True
        else:
            print("⚠️ Docker Compose not found")
            return False
    else:
        print("⚠️ Docker not found")
        return False

def main():
    """Main setup function."""
    print("🚀 Advanced Crypto Signal Detector Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Setup virtual environment
    if not setup_virtual_environment():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Setup configuration
    if not setup_configuration():
        return False
    
    # Check Docker
    docker_available = check_docker()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit config.py with your Telegram bot credentials")
    print("2. Run the detector:")
    
    if os.name == 'nt':  # Windows
        print("   • Windows: venv\\Scripts\\activate && python btc_trend_3m.py")
    else:  # Unix/Linux
        print("   • Unix/Linux: source venv/bin/activate && python btc_trend_3m.py")
    
    if docker_available:
        print("   • Docker: docker-compose up -d")
    
    print("\n📚 See README.md for detailed usage instructions")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)
