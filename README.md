Task Notification System (Clean Architecture)
Este proyecto es una API de gestión de tareas y notificaciones desarrollada bajo principios de ingeniería de software moderna. Se enfoca en la escalabilidad, el desacoplamiento de componentes y la implementación de patrones de diseño.

[!IMPORTANT]
Estado del Proyecto: 🛠️ En Formación / Académico.
Este repositorio forma parte de mi proceso de aprendizaje en Arquitectura Limpia y principios SOLID aplicado a entornos backend con Python.

Arquitectura y Principios
El proyecto está estructurado siguiendo los pilares de Clean Architecture, dividiendo las responsabilidades en capas bien definidas:

Core (Dominio): Contiene las reglas de negocio, interfaces (Protocols) y excepciones personalizadas. Es totalmente independiente de librerías externas.

Schemas (Contratos): Definición de modelos de datos utilizando Pydantic para asegurar la integridad y validación de la información (tipado estricto, UUIDs, EmailStr).

Services (Aplicación): Lógica de orquestación. Aquí se implementa el envío de notificaciones basado en prioridades.

🛠️ Patrones y SOLID Aplicado
Strategy Pattern: Implementado en el sistema de notificaciones (Whatsapp, Email, SMS, Log), permitiendo cambiar el método de envío sin alterar la lógica de negocio.

Dependency Inversion (D - SOLID): El servicio de notificaciones no depende de clases concretas, sino de abstracciones (NotifierProtocol).

Single Responsibility (S - SOLID): Cada clase tiene una única razón para cambiar; los notificadores solo envían, el manager solo normaliza y el servicio solo orquestas.

Tecnologías Utilizadas
Lenguaje: Python 3.10+

Framework: FastAPI

Validación: Pydantic (V2)

Entorno: WSL (Windows Subsystem for Linux)

Estructura del Proyecto

app/
├── api/                # configuraciones de la API

├── core/               # Reglas de negocio e Interfaces

├── schemas/            # Modelos de Pydantic (Contratos)

├── services/           # Lógica de aplicación y Estrategias

├── repositories/       # (En desarrollo) Capa de persistencia

└── main.py             # Punto de entrada de la API

Instalación (Próximamente)

Bash

git clone https://github.com/btrujillo-eng/task-notifier.git
cd task-notifier
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Notas del Autor
Como estudiante de Ingeniería de Software, mi objetivo con este repositorio es documentar mi evolución técnica, aplicando buenas prácticas de desarrollo desde las etapas iniciales del proyecto.
