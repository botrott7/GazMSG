import os, extract_msg

def main():
    '''Вытаскивает вложения любого формата кроме .png из .msg
    '''
    try:
        directory_files = str(os.getcwd()) + '/files'
        directory_results = str(os.getcwd() + '/results')

        if not os.path.exists(directory_files):
            os.makedirs(directory_files)

        if not os.path.exists(directory_results):
            os.makedirs(directory_results)

        for filename in os.listdir(directory_files):
            if not filename.endswith('.msg'):
                continue

            filepath = os.path.join(directory_files, filename)

            with extract_msg.openMsg(filepath) as msg:
                for attachment in msg.attachments:
                    if attachment.extension not in ['.png']:
                        with open(os.path.join(directory_results, attachment.name), 'wb') as f:
                            f.write(attachment.data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
