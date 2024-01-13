# Установка Arch Linux
Моя шпора для установки арча 
### Подключения wifi
```
iwctl
>station list
>station X scan
>station X get-networks
>station X connect NAME
```

### Разбивка диска на разделы
```
gdisk /dev/sdX
```
> 1G EFI (EF00) \
>8G  - SWAP (8200) \
>Other  - SYSTEM (8300)

### Форматирование
```
mkfs.fat -F32 /dev/sdX1
mkswap -L swap /dev/sdX2
swapon /dev/sdX2
mkfs.ext4 -L arch /dev/sdX3 
```
### Монтирования
```
mount /dev/sdX3 /mnt
mkdir /mnt/boot
mount /dev/sdX1 /mnt/boot
```
### Установка основных пакетов
```
pacstrap /mnt base base-devel linux linux-firmware nano
```
### Генерируем `fstab`
```
genfstab -pU /mnt >> /mnt/etc/fstab
```
### Вход в `chroot`
```
arch-chroot /mnt
```
### Установка пароля `root`
```
passwd
```
### Дать машине имя
```
nano /etc/hostname
```
### Настройка временной зони
```
ln -sf /usr/share/zoneinfo/Europe/X /etc/localtime
```
### Открыть и сгенерировать локали
```
nano /etc/locale.gen
locale-gen
```
### настройка языка консоли и шрифта
```
nano /etc/vconsole.conf
```
Код:
```
KEYMAP=ru
FONT=cyr-sun16
```
### Установка языка системы по умолчанию
```
nano /etc/locale.conf
```
Код:
```
LANG="ru_RU.UTF-8"
```
### Запуск пакетного менеджера и загрузка популярних ключей
```
pacman-key --init
pacman-key --populate archlinux
```
### Открыть `multilib`
```
nano /etc/pacman.conf
```
(multilib - раскоментировать)
### Установка базових програм
```
pacman -Sy
pacman -S bash-completion openssh networkmanager sudo git wget htop neofetch xdg-user-dirs ntfs-3g
```

mkinitcpio -p linux

### Настройка пользователя
```
nano /etc/sudoers
```
(раскоментировать wheel после root)

```
useradd -m -g users -G wheel USER
passwd USER
```
### Запуск сетевого менеджера
```
systemctl enable NetworkManager.service
```
### Загрузчик
```
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub
grub-mkconfig -o /boot/grub/grub.cfg
mkdir /boot/EFI/BOOT
cp /boot/EFI/grub/grubx64.efi /boot/EFI/BOOT/BOOTX64.efi
```

[еще не тестировал] Улучшение:
```
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=BOOT
grub-mkconfig -o /boot/grub/grub.cfg
```

### Выход
```
Ctrl+D
```
```
umount -R /mnt
reboot
```

### Установка `yay`
```
git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
```

### Названия пользовательских каталогов
```
nano ~/.config/user-dirs.dirs
```
Код:
```
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOCUMENTS_DIR="$HOME/Documents"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_MUSIC_DIR="$HOME/Music"
XDG_PICTURES_DIR="$HOME/Pictures"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_VIDEOS_DIR="$HOME/Videos"
```