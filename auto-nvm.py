
import os
import subprocess

author_name = "Bruno Sábio"
github_link = "https://github.com/sabiobru/"
linkedin_link = "https://br.linkedin.com/in/brunosabio"

print("#" * 40)
print(f"# Script: Gerenciador de Versões do Node.js")
print(f"# Autor: {author_name}")
print(f"# GitHub: {github_link}")
print(f"# LinkedIn: {linkedin_link}")
print("# Data de Criação: 10 de Setembro de 2023")
print("# Descrição: Este script permite ao usuário consultar e alternar entre diferentes versões do Node.js usando o NVM.")
print("# Este é um projeto público disponível para uso da comunidade.")
print("#" * 40)

def list_installed_versions():
    try:
        output = subprocess.check_output("node -v", shell=True, stderr=subprocess.STDOUT, text=True)
        current_version = output.strip()
        print(f"A versão atual do Node.js é: {current_version}\n")

    except subprocess.CalledProcessError as e:
        print("Erro ao verificar a versão atual do Node.js:", e.output)
        current_version = ""

    try:
        output = subprocess.check_output("nvm list", shell=True, stderr=subprocess.STDOUT, text=True)
        versions = output.split("\n")
        for i, version in enumerate(versions):
            if version.strip():
                print(f"{i} - {version.strip()}")

        print("# - Instalar outra versão")
        return current_version

    except subprocess.CalledProcessError as e:
        print("Erro ao listar as versões do Node.js:", e.output)
        return current_version

def install_version(version):
    try:
        subprocess.run(f"nvm install {version}", shell=True, check=True)
        print(f"Versão {version} instalada com sucesso!")

    except subprocess.CalledProcessError as e:
        print("Erro ao instalar a versão:", e.output)

def main():
    current_version = list_installed_versions()
    choice = input("\nEscolha uma opção (Digite o número da versão ou '#' para instalar outra): ")

    if choice == "#":
        new_version = input("Digite a versão que deseja instalar: ")
        install_version(new_version)

        use_installed = input(f"Deseja usar a versão {new_version} (y/n)? ").lower()
        if use_installed == "y":
            subprocess.run(f"nvm use {new_version}", shell=True)
        else:
            print("Fechando o terminal.")

    elif choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(current_version):
            selected_version = current_version[choice]
            subprocess.run(f"nvm use {selected_version}", shell=True)
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()

input("Pressione qualquer tecla para sair...")