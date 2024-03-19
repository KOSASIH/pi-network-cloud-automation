import os
import subprocess
import shutil

def pi_cloud_ease(config_file, image_name, work_dir, enable_cloud_services=True):
    """
    Automate cloud system management for Raspberry Pi devices, ensuring seamless operation and optimization.

    :param config_file: Path to the config file for pi-gen.
    :param image_name: Name of the output image file.
    :param work_dir: Path to the directory where the build process will take place.
    :param enable_cloud_services: If True, enable cloud services in the image.
    """

    # Check if the config file exists
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")

    # Check if the work directory exists
    if not os.path.isdir(work_dir):
        raise NotADirectoryError(f"Work directory not found: {work_dir}")

    # Clone the pi-gen repository
    subprocess.run(["git", "clone", "https://github.com/RPi-Distro/pi-gen.git"], cwd=work_dir)

    # Copy the config file to the pi-gen directory
    shutil.copy(config_file, os.path.join(work_dir, "pi-gen"))

    # Change the current directory to the pi-gen directory
    os.chdir(os.path.join(work_dir, "pi-gen"))

    # Run the build script
    subprocess.run(["./build.sh", "-c", "../config", "-o", "../deploy", "-k", "../deploy/image", "-d", "../deploy/deploy", "-s", "../deploy/stage", "-u", "../deploy/export-image", "-m", "../deploy/export-image/export-image.sh", "-e", "../deploy/export-image/export-image.sh", "-n", image_name])

    # If cloud services are enabled, copy the cloud service files to the deploy directory
    if enable_cloud_services:
        cloud_services_dir = os.path.join(work_dir, "cloud-services")
        if os.path.isdir(cloud_services_dir):
            shutil.copytree(cloud_services_dir, os.path.join(work_dir, "deploy", "cloud-services"))

    # Change the current directory back to the original directory
    os.chdir(os.path.abspath(".."))

    # Clean up the pi-gen directory
    shutil.rmtree(os.path.join(work_dir, "pi-gen"))

# Example usage
pi_cloud_ease("config.txt", "raspbian-cloud.img", "/tmp/build")
