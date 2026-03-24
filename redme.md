# 📦 Extrator de Etiquetas Shopee (A4 → 100x150mm)

Script em Python que converte etiquetas de envio da Shopee do formato **A4 (4 etiquetas por página)** para o padrão **100x150mm em PDF**, permitindo impressão em impressoras térmicas como **Tomate**, entre outras.

---

## 🚨 Problema Resolvido

A Shopee oferece dois formatos de etiquetas:

* 📄 **PDF A4 (4 etiquetas por página)** → pensado para impressoras comuns
* 🧾 **ZPL (Zebra)** → compatível com impressoras térmicas profissionais

💥 Problema:

> Impressoras térmicas mais acessíveis (como **Tomate**) **não suportam ZPL**, e o PDF A4 não é adequado para impressão direta.

👉 Resultado:

* Era necessário imprimir **uma etiqueta por vez**
* Processo lento e manual
* Baixa produtividade

---

## ✅ Solução

Este projeto resolve o problema ao:

✔️ Extrair automaticamente cada etiqueta do PDF A4
✔️ Converter para o formato **100x150mm em PDF**
✔️ Manter qualidade vetorial (QR code e código de barras perfeitos)
✔️ Permitir impressão em lote em impressoras térmicas

---

## 🚀 Funcionalidades

* 📄 Processa PDFs com múltiplas páginas
* ✂️ Divide automaticamente 4 etiquetas por página
* 📏 Converte para **100x150mm**
* 🖨️ Compatível com impressoras térmicas (Tomate, etc.)
* ⚡ Rápido e automatizado
* 🔢 Permite definir quantidade de etiquetas (evita páginas extras)

---

## 📸 Formato de Entrada

PDF padrão Shopee (A4):

```id="fmt1"
[ etiqueta 1 | etiqueta 3 ]
[ etiqueta 2 | etiqueta 4 ]
```

---

## 📤 Saída

* Uma etiqueta por página
* Formato: **100x150mm**
* Pronto para impressão direta

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* pypdf
* reportlab

---

## 📦 Instalação

```bash id="fmt2"
git clone https://github.com/DiegoMarayo/shopee-label-bridge
cd seu-repo
pip install pypdf reportlab
```

---

## ▶️ Como Usar

1. Coloque seu arquivo como:

```id="fmt3"
entrada.pdf
```

2. Execute o script:

```bash id="fmt4"
python main.py
```

3. Informe o total de etiquetas:

```id="fmt5"
Digite o total de etiquetas: 
```

4. O arquivo final será gerado:

```id="fmt6"
saida_100x150.pdf
```

---

## 🎯 Resultado

Agora você pode:

✅ Imprimir várias etiquetas de uma vez
✅ Usar impressoras térmicas sem suporte a ZPL
✅ Automatizar seu fluxo de envio
✅ Ganhar tempo e produtividade

---

## ⚠️ Observações

* A quantidade de etiquetas deve ser informada corretamente
* Isso garante que nenhuma página em branco seja gerada

---

## 💡 Melhorias Futuras

* 🔍 Detecção automática da quantidade de etiquetas
* 🌐 Interface web (upload + download)
* 🖥️ Interface gráfica (GUI)
* 📦 Empacotamento como aplicativo

---

## 👨‍💻 Autor

Projeto criado para resolver um problema real de logística no uso da Shopee com impressoras térmicas acessíveis.

---

## ⭐ Contribuição

Contribuições são bem-vindas!

* Fork do projeto
* Criação de issues
* Pull requests

---

## 📄 Licença

MIT License
