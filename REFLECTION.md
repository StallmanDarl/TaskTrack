# ICA04 Reflection

## 1. Local and Remote Repositories

What is the difference between the local TaskTrack repository and the repository hosted on GitHub?
```text
The local TaskTrack repository is the copy of the project stored on your computer. The GitHub repository is the remote copy stored online. Changes made locally must be committed and then pushed to GitHub before they appear in the remote repository.
```

## 2. Connecting and Pushing

Why did adding `origin` not immediately place the project files on GitHub?
```text
Adding `origin` only connects the local repository to the GitHub repository. It does not automatically upload any files. The project files must first be committed to Git and then pushed to the `origin` repository.
```

## 3. Cloning

How is cloning a repository different from downloading its files as a ZIP archive?
```text
Cloning creates a local Git repository that is connected to the original remote repository. This allows you to use Git to pull updates, make commits, and push changes. Downloading the project as a ZIP only gives you a copy of the files and does not include the repository's Git connection and history.
```

## 4. Fetching and Pulling

What information did `git fetch` update, and what additional action did `git pull` perform?
```text
`git fetch` updates the local repository's information about changes that exist on the remote repository without changing the current working files. `git pull` goes further by fetching the remote changes and then integrating them into the current local branch.
```

## 5. Focused Commits

Why is it useful to commit the Python feature, sample task data, and README documentation separately?
```text
Separating the Python feature, sample task data, and README documentation into different commits makes the project's history easier to understand. Each commit represents one specific change, making it easier to review changes, find problems, or undo a particular change without affecting unrelated work.
```