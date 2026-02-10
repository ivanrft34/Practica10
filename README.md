# Práctica 10: Infraestructura de Microservicios, Proxy Inverso y Caché

Este proyecto despliega una arquitectura de microservicios para la empresa "Cloud-Fast", modernizando su flujo de trabajo mediante contenedores. El objetivo es implementar seguridad perimetral, alto rendimiento mediante caché y buenas prácticas DevOps.

## 1. Descripción del Proyecto
El sistema consta de tres contenedores aislados en una red privada:
* **Nginx (Proxy Inverso):** Único punto de entrada (Puerto 80). Gestiona caché HTTP de nivel 1 (60s).
* **API Backend (Python/Flask):** Simula un proceso lento (2-3s) y conecta con Redis.
* **Redis (Base de Datos):** Almacenamiento en memoria para caché de datos persistentes (Nivel 2).

## 2. Diagrama de Arquitectura
![Diagrama de Arquitectura](ruta/a/tu/imagen-diagrama.png)
*(Nota: Debes exportar tu diagrama como imagen, subirlo al repositorio y cambiar la ruta de arriba).*

## 3. Instrucciones de Despliegue
Sigue estos pasos para levantar el entorno en tu máquina local:

### Requisitos previos
* Docker y Docker Compose instalados.
* Git instalado.

### Pasos
1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/NOMBRE_REPOSITORIO.git](https://github.com/TU_USUARIO/NOMBRE_REPOSITORIO.git)
    cd NOMBRE_REPOSITORIO
    ```

2.  **Construir y levantar los contenedores:**
    ```bash
    docker-compose up -d --build
    ```

3.  **Verificar que los contenedores están corriendo:**
    ```bash
    docker-compose ps
    ```

## 4. Pruebas de Funcionamiento y Caché
Para verificar que el sistema de caché funciona correctamente (diferencia entre MISS y HIT), puedes usar los siguientes comandos:

### Prueba 1: Primera Petición (CACHE MISS)
La primera vez, la petición tardará unos 3 segundos porque el backend debe procesarla.
```bash
time curl -I http://localhost
