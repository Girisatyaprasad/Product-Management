# Product Teardown - Spotify

## Executive summary

Spotify is an exceptional audio-streaming tool, but playback disruptions and forced algorithmic recommendations create workflow friction. This teardown investigates these reliability problems and recommends prioritizing user playback autonomy.

## **Product Overview**

Spotify is a digital audio-streaming platform providing instant access to millions of songs, podcasts, and audiobooks. 

## **Core Features**

- **Music Streaming**: A vast library of global music accessible on-demand or via custom playlists.
- **Algorithmic Personalization**: Custom discovery feeds driven by user listening habits.
- **Podcasts & Audiobooks**: Integrated spoken-word content directly alongside music tracks.
- **Cross-Device Sync**: Seamless audio handoff across phones, desktops, smart speakers, and cars.

## **Access Models**

- **Free Tier**: Ad-supported access with limited mobile skips and forced shuffle playback.
- **Premium Tier**: Paid monthly subscription unlocking offline listening, ad-free playback, and full control over song selection.

## User Segment

- Premium subscribers
- Daily commuters
- Free tier users

### Selected User Group:

Daily Commuters

## Jobs To Be Done

#### Functional Job

Daily commuters want an effortless way to listen to music that fits their preferences and current mood, making repetitive travel time more enjoyable and engaging.

#### Emotional Job

Commuters want to feel relaxed, entertained, and engaged during repetitive or boring journeys.

#### Social Job

When commuting with friends or others, users may want to share and collectively enjoy music while expressing their individual music tastes within the group.

#### Core Job

When commuting, I want an effortless way to enjoy music that matches my preferences and mood, so I can stay entertained, relaxed, and engaged throughout the journey.

## **Current Experience**

### **Strengths**

- **Effortless Discovery**: Algorithmic playlists (like *Daily Mix*) match the user's mood instantly with zero effort before starting a trip.
- **Low Decision Fatigue**: Smart recommendations fulfill the emotional job of keeping users relaxed without requiring them to manually build queues while moving.
- **Social Sharing**: Universal song links allow passengers to quickly share tracks and express their individual tastes within a commuting group.

#### **Weaknesses**

- **Forced Shuffle (Free Tier)**: Prevents commuters from choosing specific songs, which creates immense frustration when they are trying to match an exact mood for a short trip.
- **Ad Disruption**: Frequent, loud commercial breaks ruin the emotional job of staying relaxed, introducing high friction during high-stress travel.
- **Offline Instability**: Passing through dead cellular zones like tunnels or underground trains and hilly areas cuts off the stream entirely, as the Free Tier completely blocks offline song saving.

## Opportunity Areas

#### **1. AUDITORY AND COGNITIVE FRICTION**

**Aggressive Ad-Volume Spikes**

- **Description**: Programmatic audio advertisements bypass standard audio normalization and play at a significantly higher loudness level than the music tracks preceding them.
- **Impact**: Disrupts the passive commute experience. Drivers or walking commuters are forced to abruptly and manually adjust their device's master physical volume to avoid sudden ear pain. [1, 2]

#### **2. CONSTRAINT AND ECOSYSTEM FRICTION**

**The Voice Assistant Disconnect**

- **Description**: When using voice commands (Siri or Google Assistant) via Android Auto, Apple CarPlay, or headphones, requesting a specific song or playlist on the Free Tier fails to execute correctly.
- **Impact**: Because the free tier strictly forbids on-demand track selection, the assistant verbally confirms the request but actually triggers a random recommended radio station instead. This creates severe safety risks as drivers take their eyes off the road to manually fix the queue via their touchscreens. [1, 2]

#### **3. CONSTRAINT AND MODALITY FRICTION**

**The Forced-Shuffle Mood Mismatch**

- **Description**: Spotify enforces a rigid smart-shuffle constraint across the mobile free tier application.
- **Impact**: Directly fails the commuter’s emotional job of stress relief. Users seeking an exact mood to combat transit anxiety are trapped listening to random algorithmic additions. Once their strictly limited hourly skips are exhausted, they abandon the app entirely for the remainder of their journey.

## Evidence

### 1. AUDITORY FRICTION

**User Testimony — Ad Volume Spikes**

> "They are dangerously loud. I know ads are needed, but they are going to damage someone's hearing... almost every ad is 10x louder than my songs, and I like to listen to songs at a decent volume, but when an ad comes on it plays at an extremely loud volume which is very painful."
> 

> "Not only did I get blasted with SIX ads after just one song, the first ad blasted my ears so loud it still kinda hurts after two days."
> 

**Problem Classification**

- **Category:** Auditory Friction / Inconsistent Playback Volume
- **Core Issue:** Users report sudden perceived volume differences between music and advertisements. This interrupts the listening experience and forces users to manually adjust volume, which is particularly disruptive when using headphones or commuting.

### 2. VOICE ASSISTANT / HANDS-FREE FRICTION

**User Testimony — Voice Assistant Disconnect**

> "Before I updated recently to IOS 26... I used to religiously use my Siri to shuffle songs on Spotify with the 'shuffle songs by [artist] on Spotify' command."
> 

> "I tried it for the first time since updating this morning and was pretty shocked that Siri refused and said it wouldn't search anything until I wasn't driving."
> 

**Problem Classification**

- **Category:** Ecosystem Integration / Hands-Free Interaction Friction
- **Core Issue:** Some users encounter situations where voice-assistant restrictions prevent expected Spotify controls while driving, disrupting hands-free music selection.
- **Root Cause / Ownership:** Unknown. The behavior may depend partly on OS-level voice-assistant restrictions rather than Spotify itself.

### Personally Observed

“When playing favorite playlist suddenly a few ads hits like bombs, and sometimes too many ads like 3 to 4 ads in a row and ads disruption for a very few songs like only 2 or 3 songs so i’m at that point developed my own offline music app”

## **Prioritization Matrix**

| Factor | Question you're asking |
| --- | --- |
| **User impact** | How badly does this problem hurt the selected user/JTBD? |
| **Frequency** | How often does the user encounter it? |
| **Evidence strength** | How confident am I that this problem actually exists? |
| **Business impact** | If Spotify fixes it, could it meaningfully improve engagement, retention, conversion, revenue, etc.? |
| **Effort / complexity** | Roughly how difficult might solving it be? |

### Scoring Rationale

**User Impact — 4/5**

Sudden loud advertisements significantly interrupt the listening experience, particularly for users wearing headphones. This directly conflicts with the commuter JTBD of having a relaxed and engaging listening experience.

**Frequency — 3/5**

The issue appears repeatedly in user complaints and personal experience, but available evidence is insufficient to establish that it occurs frequently across Spotify's broader Free-tier user base.

**Evidence Strength — 4/5**

The problem is supported by multiple user complaints and repeated personal observation. However, no Spotify internal data or large-scale quantitative evidence is available.

**Business Impact — 5/5**

Addressing disruptive ad playback could improve satisfaction and trust among Free-tier users without necessarily removing advertising itself. Potential effects on retention, ad engagement, brand perception, and eventual Premium conversion would require validation.

**Engineering Effort — TBD / Estimated**

The internal cause and architecture are unknown. Addressing playback-volume consistency may involve Spotify's playback system, ad-delivery pipeline, audio normalization, advertiser assets, or multiple platforms. Engineering effort therefore cannot be confidently estimated from external evidence.

## Problem Selected

#### **The Programmatic Ad-Volume Spike Crisis 
(Auditory and Cognitive Friction)**

While Spotify relies on its ad-supported tier to monetize free users, a critical engineering and content delivery gap allows programmatic audio advertisements to bypass the native application's volume normalization algorithms.

**Why this problem matters:**

- **Direct Workflow Sabotage:** Some Free-tier users report advertisements playing at noticeably higher perceived volume than surrounding music, disrupting the listening experience.
- **Safety Risks:** Drivers and walking commuters are forced to take their hands or eyes off their surroundings to grab their physical devices and turn down the volume, presenting a real-world safety hazard.
- **Value Erosion:** Rather than nudging users to convert to Premium through feature delight, this friction forces users to mute their devices, close the app entirely, or associate the advertised brands with frustration, directly destroying long-term advertiser value and user retention.

## Success Metrics

#### Primary Success Metrics

- Percentage of ad impressions followed by a manual volume decrease within a defined time window after the ad begins.
- A reduction would indicate fewer disruptive volume transitions between music and advertisements.

#### Secondary Success Metrics

- Percentage of listening sessions where users stop playback or leave Spotify shortly after an advertisement begins.
- Lower rates may indicate a less disruptive advertising experience.
- Percentage of users leaving/stopping playback shortly after an ad begins will be reduced.

#### Guardrail Metric

- Ensure improved volume consistency does not reduce ad completion.

## 

## Risks & Constraints

### Risks

- Volume normalization may overcorrect properly mixed ads, making them unnecessarily quiet.
- Excessive normalization could reduce ad clarity or effectiveness for advertisers.
- Reducing ad frequency may require longer ad breaks or reduce available advertising inventory.

### Constraints

- Changes must work consistently across Spotify's ad-delivery systems and supported platforms.
- The solution may depend on audio-processing and ad-delivery systems rather than simple UI changes.
- Implementation may depend partly on the audio assets and requirements provided by advertising partners.

## Recommendation

I recommend Spotify reduce excessive ad frequency to healthier levels and improve its ad-delivery systems to maintain consistent volume across advertisements. Spotify should also work with advertising partners to establish audio requirements that create a better listening experience while preserving high-quality advertising value for both Spotify and its partners.
