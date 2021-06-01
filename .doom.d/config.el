;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "Halvard Samdal"
      user-mail-address "samdal@protonmail.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:
;; (setq doom-font (font-spec :family "monospace" :size 12 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "sans" :size 13))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)


;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.


;; Setting the font
(setq  doom-font (font-spec :family "iosevka" :size 17))

;; Setting theme
(setq doom-theme 'doom-gruvbox)

;(require 'elcord)
;(elcord-mode)

;;(after! lsp-rust
;;  (setq lsp-rust-server 'rust-analyzer))


(defun franco/godot-gdscript-lsp-ignore-error (original-function &rest args)
  "Ignore the error message resulting from Godot not replying to the `JSONRPC' request."
  (if (string-equal major-mode "gdscript-mode")
      (let ((json-data (nth 0 args)))
        (if (and (string= (gethash "jsonrpc" json-data "") "2.0")
                 (not (gethash "id" json-data nil))
                 (not (gethash "method" json-data nil)))
            nil ; (message "Method not found")
          (apply original-function args)))
    (apply original-function args)))
(advice-add #'lsp--get-message-type :around #'franco/godot-gdscript-lsp-ignore-error)

(setq display-line-numbers-type 'relative)

(setq c-default-style "gnu")

(setq flycheck-clang-include-path '("/home/halvard/Code/gdnative_cpp_example/godot-cpp/include/core/"
                                    "/home/halvard/Code/gdnative_cpp_example/godot-cpp/include/gen/"
                                    "/home/halvard/Code/gdnative_cpp_example/godot-cpp/include/"
                                    "/home/halvard/Code/gdnative_cpp_example/godot-cpp/godot-headers/"))

(setq irony-additional-clang-options '("-I/home/halvard/Code/gdnative_cpp_example/godot-cpp/include/core/"
                                       "-I/home/halvard/Code/gdnative_cpp_example/godot-cpp/include/gen/"
                                       "-I/home/halvard/Code/gdnative_cpp_example/godot-cpp/include/"
                                       "-I/home/halvard/Code/gdnative_cpp_example/godot-cpp/godot-headers/"))

(setq flycheck-gcc-args '("-I/home/halvard/Code/Arduino/chickendoor/include"
                                       "-I/home/halvard/Code/Arduino/chickendoor/src"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/cores/arduino"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/variants/eightanaloginputs"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/libraries/EEPROM/src"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/libraries/HID/src"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/libraries/SPI/src"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/libraries/SoftwareSerial/src"
                                       "-I/home/halvard/.platformio/packages/framework-arduino-avr/libraries/Wire/src"
                                       "-I/home/halvard/.platformio/packages/toolchain-atmelavr/lib/gcc/avr/7.3.0/include-fixed"
                                       "-I/home/halvard/.platformio/packages/toolchain-atmelavr/lib/gcc/avr/7.3.0/include"
                                       "-I/home/halvard/.platformio/packages/toolchain-atmelavr/avr/include"
                                       "-I/home/halvard/.platformio/packages/tool-unity"
                                        "-DPLATFORMIO=50101"
                                        "-DARDUINO_AVR_PRO"
                                        "-DF_CPU=16000000L"
                                        "-DARDUINO_ARCH_AVR"
                                        "-DARDUINO=10808"
                                        "-D__AVR_ATmega328P__"))

(require 'flycheck-arduino)
(add-hook 'arduino-mode-hook #'flycheck-arduino-setup)
(require 'company-tabnine)
(add-to-list 'company-backends #'company-tabnine)
;; Trigger completion immediately.
(setq company-idle-delay 0)
;; Number the candidates (use M-1, M-2 etc to select completions).
(setq company-show-numbers t)

