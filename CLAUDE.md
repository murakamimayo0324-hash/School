# School プロジェクト

Claude Code のプロジェクト設定（Skills / Agents / Settings）を管理するリポジトリ。

## プロジェクト構成

- `CLAUDE.md` — このファイル。プロジェクトメモリ（セッション開始時に自動読み込み）
- `.claude/settings.json` — 権限などのプロジェクト共有設定（コミット対象）
- `.claude/settings.local.json` — マシンローカルの上書き設定（gitignore 対象）
- `.claude/skills/` — カスタム Skill（スラッシュコマンド）
- `.claude/agents/` — カスタムサブエージェント

## 利用できる Skill

### /summarize-file
指定したファイルを読み込み、次の形式で日本語の要約と改善提案を出力する:

- **タイトル**（1 行）
- **トピック**（必ず 3 つ）
- **結論**（1〜3 文）
- **改善提案**（構成・誤字の観点で必ず 3 つ）

使い方: `/summarize-file <ファイルパス>`（例: `/summarize-file docs/note.md`）

定義: `.claude/skills/summarize-file/SKILL.md`

## 利用できる Agent

### claude-code-guide
Claude Code / Agent SDK / Claude API に関する質問へ、公式ドキュメントを調査して回答する読み取り専用エージェント。
Skill や Agent、settings.json を新規作成・変更するときは、先にこのエージェントで正しい形式を確認すること。

定義: `.claude/agents/claude-code-guide.md`

## 運用ルール

- 新しいスラッシュコマンドは `.claude/commands/`（非推奨）ではなく `.claude/skills/<name>/SKILL.md` に作成する
- Skill のトピック数・出力形式など仕様変更は SKILL.md の「出力形式」セクションを更新する
- 要約はファイルに書かれている内容のみに基づき、推測で補わない
