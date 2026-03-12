import os
import shutil
import random
import string
import sys

def get_random_name(max_len=7):
    """Generates a random string of up to max_len characters."""
    # Generate a random number between 1 and max_len for length
    length = random.randint(1, max_len)
    
    # Character pool: uppercase letters, lowercase letters, and digits
    chars_pool = string.ascii_letters + string.digits
    
    # Select random characters
    return ''.join(random.choices(chars_pool, k=length))

def rename_and_sort_files(source_dir):
    """
    Moves all files from a folder into subdirectories based on their extension,
    renaming them with the format [Random].[OriginalExtension].
    Prevents processing itself if it resides in the same folder.
    """
    
    print(f"Starting analysis in: {source_dir}")
    
    # Safety check: Is this script running inside its own target directory?
    script_filename = os.path.basename(sys.argv[0])
    if os.path.abspath(source_dir) == os.path.dirname(os.path.abspath(script_filename)):
        print("⚠️  CRITICAL WARNING: Script detected it is executing within the destination directory.")
        confirm = input("Are you sure you want to continue? This could delete or corrupt the script itself. (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled for safety reasons.")
            return

    # Step 1: Collect unique extensions
    extensions = []
    for item in os.listdir(source_dir):
        file_path = os.path.join(source_dir, item)
        
        # Skip directories and symbolic links
        if not os.path.isfile(file_path):
            continue
            
        _, ext = os.path.splitext(item)
        clean_ext = ext[1:] if ext.startswith('.') else ext
        
        if clean_ext and clean_ext not in extensions:
            extensions.append(clean_ext)

    if not extensions:
        print("No files with valid extensions found to process.")
        return

    print(f"✅ Found {len(extensions)} unique extensions.\n")

    # Create subfolders
    print("Creating folder structure...")
    for ext in extensions:
        folder_name = f".{ext}"
        target_folder = os.path.join(source_dir, folder_name)
        if not os.path.exists(target_folder):
            try:
                os.makedirs(target_folder)
                print(f"   - Created: {folder_name}")
            except OSError as e:
                print(f"   ⚠️  Error creating {folder_name}: {e}")

    # Step 2: Move and rename files
    print("\n🔄 Processing and moving files...\n")
    
    moved_count = 0
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if not os.path.isfile(file_path):
            continue
        
        _, orig_ext = os.path.splitext(filename)
        clean_orig_ext = orig_ext[1:] if orig_ext.startswith('.') else orig_ext
        
        # Safety check: Ignore Python scripts and names similar to the script
        # This prevents the script from deleting itself or creating infinite loops with other scripts
        is_script_target = (
            filename.lower().endswith('.py') or 
            'sorter' in filename.lower() or 
            'script' in filename.lower()
        )
        
        if is_script_target:
            print(f"🛡️  Protecting/Skipping system/cripto file: {filename}")
            continue
            
        if not clean_orig_ext:
            print(f"⏭️  Skipping file without extension: {filename}")
            continue
        
        # Generate new name
        random_part = get_random_name(max_len=7)
        
        # --- CORRECTED LOGIC HERE ---
        # Explicitly adds a dot "." before the original extension
        new_filename = f"{random_part}.{clean_orig_ext}"
        # -----------------------------
        
        folder_name = f".{clean_orig_ext}"
        target_folder = os.path.join(source_dir, folder_name)
        destination_path = os.path.join(target_folder, new_filename)
        
        try:
            shutil.move(file_path, destination_path)
            moved_count += 1
        except PermissionError:
            print(f"❌ Permission failed for: {filename}")
        except Exception as e:
            print(f"❌ Unexpected error with {filename}: {e}")

    print(f"\n✨ Process completed! {moved_count} files have been moved.")

if __name__ == "__main__":
    print("="*60)
    print(" 📁 ADVANCED FILE ORGANIZER")
    print("="*60)
    
    directory_to_process = input("\nEnter the full path of the directory to organize: ").strip()
    
    if not os.path.isdir(directory_to_process):
        print(f"❌ ERROR: Path '{directory_to_process}' is invalid or does not exist.")
        sys.exit(1)
        
    confirm = input("\n⚠️  WARNING: This operation moves and renames files permanently.\nContinue? (y/n): ")
    if confirm.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)
        
    rename_and_sort_files(directory_to_process)