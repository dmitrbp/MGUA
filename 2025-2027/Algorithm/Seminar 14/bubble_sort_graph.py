import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors

# Настройка стиля
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'sans-serif'


class BubbleSortVisualizer:
    def __init__(self, arr):
        self.arr = arr.copy()
        self.n = len(arr)
        self.steps = []  # Сохраняем состояние на каждом шаге
        self.compare_indices = []  # Сохраняем индексы сравниваемых элементов
        self.swap_indices = []  # Сохраняем индексы меняемых элементов
        self.comparisons = 0
        self.swaps = 0

        # Генерируем все шаги алгоритма
        self._generate_steps()

        # Настройка графики
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(14, 10),
                                                      gridspec_kw={'height_ratios': [3, 1]})
        self.fig.patch.set_facecolor('#f0f2f5')

    def _generate_steps(self):
        """Генерирует все шаги сортировки для анимации"""
        arr = self.arr.copy()
        n = len(arr)

        # Сохраняем начальное состояние
        self.steps.append(arr.copy())
        self.compare_indices.append((-1, -1))
        self.swap_indices.append((-1, -1))

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                self.comparisons += 1

                # Сохраняем состояние перед сравнением
                self.steps.append(arr.copy())
                self.compare_indices.append((j, j + 1))
                self.swap_indices.append((-1, -1))

                if arr[j] > arr[j + 1]:
                    # Сохраняем состояние перед обменом
                    self.steps.append(arr.copy())
                    self.compare_indices.append((j, j + 1))
                    self.swap_indices.append((j, j + 1))

                    # Выполняем обмен
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.swaps += 1
                    swapped = True

                    # Сохраняем состояние после обмена
                    self.steps.append(arr.copy())
                    self.compare_indices.append((-1, -1))
                    self.swap_indices.append((-1, -1))

            # Сохраняем состояние после завершения прохода
            if i < n - 1:
                self.steps.append(arr.copy())
                self.compare_indices.append((-1, -1))
                self.swap_indices.append((-1, -1))

            if not swapped:
                break

        # Сохраняем финальное состояние
        if self.steps[-1] != arr:
            self.steps.append(arr.copy())
            self.compare_indices.append((-1, -1))
            self.swap_indices.append((-1, -1))

    def draw_bars(self, ax, arr, compare_idx=(-1, -1), swap_idx=(-1, -1), step_num=0):
        """Отрисовывает столбчатую диаграмму"""
        ax.clear()

        # Создаем цвета для столбцов
        colors = []
        for i in range(len(arr)):
            if i in compare_idx:
                colors.append('#ff6b6b')  # Красный для сравнения
            elif i in swap_idx:
                colors.append('#ffd93d')  # Желтый для обмена
            else:
                # Градиент от синего к зеленому в зависимости от значения
                normalized = arr[i] / max(arr) if max(arr) > 0 else 0
                colors.append(plt.cm.viridis(normalized))

        # Рисуем столбцы
        bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black',
                      linewidth=1.5, alpha=0.85)

        # Добавляем значения на столбцы
        for i, (bar, val) in enumerate(zip(bars, arr)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + max(arr) * 0.02,
                    f'{val}', ha='center', va='bottom', fontweight='bold', fontsize=10)

        # Настройка графика
        ax.set_xlabel('Индекс элемента', fontsize=12, fontweight='bold')
        ax.set_ylabel('Значение', fontsize=12, fontweight='bold')
        ax.set_title(f'Сортировка пузырьком - Шаг {step_num}',
                     fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(range(len(arr)))
        ax.set_xticklabels(range(len(arr)))
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_ylim(0, max(arr) * 1.15)

        # Добавляем легенду
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#ff6b6b', label='Сравниваемые элементы'),
            Patch(facecolor='#ffd93d', label='Меняемые элементы'),
            Patch(facecolor='#2ecc71', label='Остальные элементы')
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

        return bars

    def draw_stats(self, ax, step_num):
        """Отрисовывает статистику"""
        ax.clear()
        ax.axis('off')

        # Создаем информационную панель
        total_steps = len(self.steps)
        progress = (step_num / total_steps) * 100

        info_text = f"""
        ╔══════════════════════════════════════════════════════════╗
        ║                  📊 СТАТИСТИКА СОРТИРОВКИ                 ║
        ╠══════════════════════════════════════════════════════════╣
        ║  Текущий шаг:        {step_num}/{total_steps}                         
        ║  Прогресс:           {progress:.1f}%                                     
        ║  Всего сравнений:    {self.comparisons}                                    
        ║  Всего обменов:      {self.swaps}                                        
        ║  Размер массива:     {self.n}                                          
        ╚══════════════════════════════════════════════════════════╝
        """

        ax.text(0.5, 0.5, info_text, transform=ax.transAxes,
                fontsize=11, verticalalignment='center',
                horizontalalignment='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        # Добавляем прогресс-бар
        if progress > 0:
            from matplotlib.patches import Rectangle
            bar_ax = ax.inset_axes([0.2, 0.15, 0.6, 0.05])
            bar_ax.add_patch(Rectangle((0, 0), progress / 100, 1,
                                       facecolor='#2ecc71', edgecolor='black'))
            bar_ax.set_xlim(0, 1)
            bar_ax.set_ylim(0, 1)
            bar_ax.axis('off')
            bar_ax.set_title('Прогресс сортировки', fontsize=10, pad=5)

    def update_frame(self, frame):
        """Обновляет кадр анимации"""
        if frame >= len(self.steps):
            return

        # Отрисовываем столбцы
        arr = self.steps[frame]
        compare_idx = self.compare_indices[frame]
        swap_idx = self.swap_indices[frame]

        self.draw_bars(self.ax1, arr, compare_idx, swap_idx, frame)
        self.draw_stats(self.ax2, frame)

        # Добавляем заголовок с описанием действия
        if compare_idx[0] != -1 and swap_idx[0] != -1:
            action_text = f"🔄 Обмен: {arr[swap_idx[0]]} ↔ {arr[swap_idx[1]]}"
        elif compare_idx[0] != -1:
            action_text = f"🔍 Сравнение: {arr[compare_idx[0]]} и {arr[compare_idx[1]]}"
        else:
            action_text = "✓ Завершение прохода..."

        self.fig.suptitle(f'Сортировка пузырьком - {action_text}',
                          fontsize=16, fontweight='bold', y=0.98)

        plt.tight_layout()

    def animate(self, interval=800):
        """Запускает анимацию"""
        anim = animation.FuncAnimation(
            self.fig, self.update_frame, frames=len(self.steps),
            interval=interval, repeat=False, cache_frame_data=False
        )

        plt.show()
        return anim


def interactive_menu():
    """Интерактивное меню с красивым интерфейсом"""
    print("\n" + "=" * 60)
    print("🎨     СОРТИРОВКА ПУЗЫРЬКОМ С ВИЗУАЛИЗАЦИЕЙ     🎨")
    print("=" * 60)

    while True:
        print("\n📋 Выберите способ создания массива:")
        print("  1. ✍️  Ввести свой массив")
        print("  2. 🎲  Случайный массив")
        print("  3. 📚  Предустановленные примеры")
        print("  4. 📈  Специальные тестовые случаи")
        print("  5. 🚪  Выход")

        choice = input("\n👉 Ваш выбор (1-5): ").strip()

        if choice == '1':
            try:
                arr_input = input("Введите числа через пробел: ")
                arr = [int(x) for x in arr_input.split()]
                if not arr:
                    print("❌ Массив не может быть пустым!")
                    continue
                if len(arr) > 30:
                    print("⚠️  Для лучшей визуализации рекомендуется массив до 30 элементов")
                return arr
            except ValueError:
                print("❌ Ошибка! Введите целые числа через пробел.")

        elif choice == '2':
            try:
                size = int(input("Введите размер массива (5-50): "))
                size = max(5, min(50, size))
                min_val = int(input("Минимальное значение (по умолчанию 1): ") or "1")
                max_val = int(input("Максимальное значение (по умолчанию 100): ") or "100")
                arr = [random.randint(min_val, max_val) for _ in range(size)]
                print(f"✅ Сгенерирован массив: {arr[:10]}{'...' if size > 10 else ''}")
                return arr
            except ValueError:
                print("❌ Ошибка! Введите корректные числа.")

        elif choice == '3':
            print("\n📚 Предустановленные примеры:")
            print("  a) [64, 34, 25, 12, 22, 11, 90] - Обычный массив")
            print("  b) [1, 2, 3, 4, 5, 6, 7, 8] - Уже отсортированный")
            print("  c) [9, 8, 7, 6, 5, 4, 3, 2, 1] - Обратный порядок")
            print("  d) [5, 1, 4, 2, 8, 3, 7, 6] - Почти отсортированный")
            print("  e) [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Полная инверсия")

            ex_choice = input("Выберите пример (a-e): ").lower()
            examples = {
                'a': [64, 34, 25, 12, 22, 11, 90],
                'b': [1, 2, 3, 4, 5, 6, 7, 8],
                'c': [9, 8, 7, 6, 5, 4, 3, 2, 1],
                'd': [5, 1, 4, 2, 8, 3, 7, 6],
                'e': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            }
            if ex_choice in examples:
                return examples[ex_choice]
            else:
                print("❌ Неверный выбор! Использую пример 'a'")
                return examples['a']

        elif choice == '4':
            print("\n📈 Специальные тестовые случаи:")
            print("  1. Массив с дубликатами")
            print("  2. Массив с отрицательными числами")
            print("  3. Массив из 2 элементов")
            print("  4. Массив из 1 элемента")

            test_choice = input("Ваш выбор (1-4): ")
            if test_choice == '1':
                return [5, 2, 8, 2, 9, 1, 5, 5, 3]
            elif test_choice == '2':
                return [-5, 3, -1, 8, -2, 0, 4, -3]
            elif test_choice == '3':
                return [42, 24]
            elif test_choice == '4':
                return [100]
            else:
                print("❌ Неверный выбор!")

        elif choice == '5':
            print("\n👋 До свидания!")
            exit()
        else:
            print("❌ Неверный выбор! Попробуйте снова.")


def main():
    """Главная функция"""
    try:
        # Получаем массив от пользователя
        arr = interactive_menu()

        print(f"\n📊 Исходный массив: {arr}")
        print(f"🔢 Размер массива: {len(arr)}")

        # Настройка анимации
        print("\n⚙️  Настройка анимации:")
        print("  1. 🐢 Медленно (1.2 сек между шагами)")
        print("  2. 🚶 Средне (0.8 сек)")
        print("  3. 🏃 Быстро (0.4 сек)")
        print("  4. ⚡ Очень быстро (0.2 сек)")

        speed_choice = input("Ваш выбор (1-4): ")
        speed_map = {'1': 1200, '2': 800, '3': 400, '4': 200}
        interval = speed_map.get(speed_choice, 800)

        # Создаем визуализатор
        print("\n🎬 Запуск визуализации...")
        visualizer = BubbleSortVisualizer(arr)

        print(f"📈 Сгенерировано {len(visualizer.steps)} шагов анимации")
        print("🎨 Закрытие окна с графикой завершит программу")
        print("✨ Наслаждайтесь визуализацией!\n")

        # Запускаем анимацию
        visualizer.animate(interval=interval)

    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем.")
    except Exception as e:
        print(f"\n❌ Произошла ошибка: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()