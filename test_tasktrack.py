from tasktrack import remove_task_by_number

def test_remove_first_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Study"

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Exercise", "Read"]


def test_remove_middle_task():
    """Removing task 2 should remove the middle task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Exercise"

    # Act
    removed_task = remove_task_by_number(tasks, 2)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Read"]


def test_remove_last_task():
    """Removing the last task should remove and return it."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Read"

    # Act
    removed_task = remove_task_by_number(tasks, len(tasks))

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Exercise"]


def test_reject_zero_task_number():
    """Task number 0 should return None without changing the list."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    original_tasks = tasks.copy()

    # Act
    removed_task = remove_task_by_number(tasks, 0)

    # Assert
    assert removed_task is None
    assert tasks == original_tasks


def test_reject_task_number_greater_than_list_length():
    """An out-of-range task number should not change the list."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    original_tasks = tasks.copy()

    # Act
    removed_task = remove_task_by_number(tasks, len(tasks) + 1)

    # Assert
    assert removed_task is None
    assert tasks == original_tasks

def test_remove_task_from_empty_list():
    """Removing a task from an empty list should return None."""
    # Arrange
    tasks = []

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task is None
    assert tasks == []
