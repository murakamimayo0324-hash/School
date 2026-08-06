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

### /build-and-review
実装タスクを Analyzer → Builder → Reviewer のパイプラインで順次実行する（差し戻しは最大 2 回）。

使い方: `/build-and-review <タスクの説明>`（例: `/build-and-review 電卓スクリプトにべき乗機能を追加`）

定義: `.claude/skills/build-and-review/SKILL.md`

### その他の Skill(他ブランチから集約)

- `/char-count` — テキストの文字数を 4 パターンでカウント(`.claude/skills/char-count/SKILL.md`)
- `/meeting-notes-template` — テンプレートから議事録を作成(`.claude/skills/meeting-notes-template/SKILL.md`)
- `/goal-prompt-builder` — /goal 用の完成条件プロンプトを作成(`.claude/skills/goal-prompt-builder/SKILL.md`)
- `/voice-to-goal` — 音声入力の文字起こしを /goal プロンプトへ整形(`.claude/skills/voice-to-goal/SKILL.md`)

## 利用できる Agent

### claude-code-guide
Claude Code / Agent SDK / Claude API に関する質問へ、公式ドキュメントを調査して回答する読み取り専用エージェント。
Skill や Agent、settings.json を新規作成・変更するときは、先にこのエージェントで正しい形式を確認すること。

定義: `.claude/agents/claude-code-guide.md`

### 開発パイプライン: Analyzer → Builder → Reviewer → 完成
実装タスクを 3 段階で進めるサブエージェント群。必ずこの順で直列に実行する。

1. **analyzer**（読み取り専用）— 依頼と現状を調査し、完成条件・変更方針をまとめた「分析レポート」を作成
2. **builder**（編集可）— 分析レポートの方針どおりに実装し、「実装結果レポート」を作成
3. **reviewer**（読み取り専用）— 完成条件と実装を突き合わせ、「✅ 完成」または「❌ 差し戻し（修正指示付き）」を判定。差し戻し時は builder に戻す（上限 2 回を目安）

定義: `.claude/agents/analyzer.md` / `.claude/agents/builder.md` / `.claude/agents/reviewer.md`

### code-reviewer
単発・パイプライン外のコード品質レビュー（セキュリティ → バグ → スタイルの順で指摘、修正はしない読み取り専用）。
パイプラインの完成判定には reviewer を使い、こちらは使わない。

定義: `.claude/agents/code-reviewer.md`

### doc-generator
コードを解析して README・docstring・API 仕様などのドキュメント内容を生成する読み取り専用エージェント。
ファイルには書き込まないため、生成結果の反映は builder か手動で行う。

定義: `.claude/agents/doc-generator.md`

### test-runner
テストフレームワークを検出してテストを実行し、失敗の根本原因を診断・報告するエージェント（ソースの修正はしない）。

定義: `.claude/agents/test-runner.md`

## 運用ルール

- 新しいスラッシュコマンドは `.claude/commands/`（非推奨）ではなく `.claude/skills/<name>/SKILL.md` に作成する
- Skill のトピック数・出力形式など仕様変更は SKILL.md の「出力形式」セクションを更新する
- 要約はファイルに書かれている内容のみに基づき、推測で補わない
