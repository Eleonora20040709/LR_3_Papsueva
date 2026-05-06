#!/bin/bash
echo '#!/bin/bash' > testfile.sh
echo 'echo "Это testfile, созданный из Papsueva2.sh"' » testfile.sh
echo 'echo "Текущая дата: $(date)"' » testfile.sh
chmod +x testfile.sh

echo ""
echo "Список файлов в каталоге (длинный формат):"
ls -l

echo ""
echo "Скрипт testfile.sh создан. Запустите его: ./testfile.sh"