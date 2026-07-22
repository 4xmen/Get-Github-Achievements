# English Learning Studio 技术方案

## 1. 项目定位

English Learning Studio 是一个面向英语学习的视频精听训练软件。

核心目标：

* 导入英语学习视频
* 播放视频并同步显示音频波形
* 支持精确选择学习片段
* 对片段进行循环播放训练
* 支持字幕同步
* 保存学习记录
* 后期扩展 AI 听写、跟读评分、智能切句等功能

软件定位：

> 一个集视频播放器、音频分析工具和英语训练平台于一体的智能学习工作台。

---

# 2. 技术方案

## 2.1 总体技术栈

采用：

```
Rust + QML + FFmpeg + SQLite
```

架构：

```
┌────────────────────────────┐
│          QML UI             │
│                             │
│ VideoView                   │
│ WaveformView                │
│ SubtitleView                │
│ ControlPanel                │
│                             │
└──────────────┬─────────────┘
               │
               │ Qt/Rust Interface
               │
┌──────────────▼─────────────┐
│          Rust Core          │
│                             │
│ MediaController             │
│ WaveformEngine              │
│ SubtitleManager             │
│ LearningManager             │
│ DatabaseManager             │
│                             │
└──────────────┬─────────────┘
               │
               │ FFmpeg Binding
               │
┌──────────────▼─────────────┐
│          FFmpeg             │
│                             │
│ libavformat                 │
│ libavcodec                  │
│ libswscale                  │
│ libswresample               │
│                             │
└────────────────────────────┘
```

---

# 3. 模块职责

## 3.1 QML UI 层

负责：

* 用户界面
* 动画效果
* 鼠标交互
* 波形选择
* 视频控制按钮

主要组件：

```
qml/

├── Main.qml
├── VideoView.qml
├── WaveformView.qml
├── SubtitleView.qml
└── ControlPanel.qml
```

---

## 3.2 Rust核心层

Rust负责业务逻辑。

主要模块：

```
src/

├── media/
│   ├── player.rs
│   └── decoder.rs
│
├── waveform/
│   ├── generator.rs
│   └── analyzer.rs
│
├── subtitle/
│   └── parser.rs
│
├── learning/
│   ├── segment.rs
│   └── manager.rs
│
└── database/
    └── sqlite.rs
```

---

# 4. 音视频处理架构

## 4.1 FFmpeg作用

FFmpeg作为底层媒体引擎。

负责：

* 视频文件解析
* 视频解码
* 音频解码
* 音频格式转换

支持：

```
mp4
mkv
mov
avi
webm
```

支持编码：

```
H264
H265
AAC
MP3
Opus
```

---

## 4.2 FFmpeg模块

主要使用：

### libavformat

作用：

解析媒体文件。

流程：

```
video.mp4

↓

libavformat

↓

video stream

audio stream

subtitle stream
```

---

### libavcodec

作用：

视频、音频解码。

流程：

```
H264

↓

AVFrame

↓

图像数据
```

---

### libswscale

作用：

图像格式转换。

例如：

```
YUV

↓

RGB

↓

QML显示
```

---

### libswresample

作用：

音频格式转换。

例如：

```
AAC

↓

PCM

↓

波形分析
```

---

# 5. 播放模块设计

## MediaController

负责：

* 打开视频
* 播放
* 暂停
* 跳转
* 倍速

Rust结构：

```rust
pub struct MediaController {

    duration: f64,

    position: f64,

}
```

接口：

```rust
impl MediaController {

    pub fn open(path:String);

    pub fn play();

    pub fn pause();

    pub fn seek(time:f64);

}
```

---

# 6. Waveform波形系统

## 6.1 功能

显示：

* 音频强度
* 语音停顿
* 句子长度
* 当前播放位置

示例：

```
时间轴

0s                 30s

|--------------------|

     /\      /\
____/  \____/  \_____
```

---

## 6.2 波形生成流程

```
video.mp4

↓

FFmpeg

↓

PCM音频

↓

Rust音频分析

↓

Waveform数据

↓

QML绘制
```

数据：

```rust
Vec<f32>
```

例如：

```
[
0.2,
0.5,
0.8,
0.3
]
```

---

# 7. 片段循环训练系统

## Segment结构

一个学习片段：

```rust
struct Segment {

    start_time:f64,

    end_time:f64,

    repeat_count:u32

}
```

例如：

```
视频：

TED_AI.mp4


训练片段：

10.5s - 18.2s


重复：

20次
```

---

## 循环逻辑

播放：

```
start

↓

播放

↓

end

↓

seek(start)

↓

继续播放
```

---

# 8. 字幕系统

支持：

```
.srt
.ass
.vtt
```

数据结构：

```rust
struct Subtitle {

    start:f64,

    end:f64,

    text:String

}
```

显示：

```
10.5s

Hello everyone.

大家好。
```

---

# 9. 学习记录系统

采用：

```
SQLite
```

---

## Video表

```sql
CREATE TABLE video(

id INTEGER PRIMARY KEY,

path TEXT,

duration REAL

);
```

---

## Segment表

```sql
CREATE TABLE segment(

id INTEGER PRIMARY KEY,

video_id INTEGER,

start_time REAL,

end_time REAL,

repeat_count INTEGER

);
```

---

## Vocabulary表

```sql
CREATE TABLE vocabulary(

id INTEGER PRIMARY KEY,

word TEXT,

meaning TEXT,

timestamp REAL

);
```

---

# 10. AI扩展方向

## 10.1 Whisper自动切句

流程：

```
视频

↓

Whisper

↓

语音识别

↓

时间戳字幕

↓

自动生成学习片段
```

效果：

```
Sentence 1

Hello everyone.

00:10.2 - 00:12.5


Sentence 2

Today we learn AI.

00:12.5 - 00:16.8
```

---

## 10.2 跟读评分

流程：

```
学生录音

↓

语音识别

↓

音素分析

↓

评分

↓

反馈
```

评价：

* 发音
* 语速
* 重音
* 流畅度

---

# 11. 项目目录设计

```
EnglishLearningStudio/

├── Cargo.toml
│
├── src/
│
│── main.rs
│
├── media/
│   ├── player.rs
│   └── decoder.rs
│
├── waveform/
│   ├── generator.rs
│   └── analyzer.rs
│
├── subtitle/
│   └── parser.rs
│
├── learning/
│   ├── segment.rs
│   └── manager.rs
│
├── database/
│   └── sqlite.rs
│
└── qml/

    ├── Main.qml
    ├── VideoView.qml
    ├── WaveformView.qml
    └── Controls.qml
```

---

# 12. 开发路线

## 第一阶段：基础播放器

目标：

完成：

* QML界面
* 视频播放
* 暂停
* seek

---

## 第二阶段：波形系统

完成：

* 音频提取
* PCM分析
* 波形显示
* 播放位置同步

---

## 第三阶段：英语学习功能

完成：

* 区域选择
* 循环播放
* 保存训练片段
* 学习记录

---

## 第四阶段：AI增强

完成：

* Whisper字幕生成
* 自动切句
* 单词提取
* 跟读评分

---

# 13. 最终产品形态

```
┌──────────────────────┐
│                      │
│       视频窗口        │
│                      │
├──────────────────────┤
│ ~~~/\~~~~/\~~~~       │
│        ↑             │
│     当前播放位置      │
├──────────────────────┤
│ Hello everyone       │
│ 大家好               │
├──────────────────────┤
│ ▶  🔁 0.8x 保存片段   │
└──────────────────────┘
```

---

# 14. 技术选择总结

| 模块   | 技术                                |
| ---- | --------------------------------- |
| 界面   | Qt QML                            |
| 核心逻辑 | Rust                              |
| 视频处理 | FFmpeg                            |
| 音频分析 | Rust + FFmpeg                     |
| 波形绘制 | QML Canvas / Qt Quick Scene Graph |
| 数据库  | SQLite                            |
| AI识别 | Whisper                           |
| 构建系统 | Cargo + CMake                     |

---

## 项目目标

打造一个：

> 基于 Rust + QML + FFmpeg 的 AI 英语精听训练平台。

核心创新点：

**以音频波形为中心，把视频内容转换成可重复训练的语言学习单元。**
