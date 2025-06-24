# Contagem de Objetos com OpenCV

Este projeto realiza a **detecção e contagem de objetos** em imagens utilizando técnicas avançadas de **processamento de imagem** com a biblioteca OpenCV. A aplicação identifica objetos mesmo quando estão **colados ou sobrepostos**, como no exemplo com chocolates.

---

## Funcionalidades

- ✅ Conversão para escala de cinza e equalização de histograma  
- ✅ Binarização automática com **Otsu**  
- ✅ Remoção de ruídos com **operações morfológicas**  
- ✅ Separação de objetos colados com **Transformada de Distância** e **Watershed**  
- ✅ Filtro de contornos pequenos para ignorar ruídos irrelevantes  
- ✅ Exibição do número total de objetos detectados na imagem  
- ✅ Salvamento da imagem final com contornos e texto  

---

## Exemplo

- **Imagem de entrada:**  
  `images/chocolates.jpg`  

- **Imagem gerada com objetos detectados:**  
  `images/result_chocolates.png`  

---

## Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/fer-oliveiraa/contagem-objetos-opencv.git
   cd contagem-objetos-opencv

2. Instale as dependências:

    ```bash
    pip install opencv-python numpy

Certifique-se de que a imagem chocolates.jpg esteja dentro da pasta images/.

3. Execute o script:

      ```bash
      python main.py

