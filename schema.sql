-- SummerSuite database schema
-- Exported from Supabase. Reflects table structure only — no user data.

CREATE TABLE public.users (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  created_at timestamp with time zone DEFAULT now(),
  name text NOT NULL,
  age integer NOT NULL,
  gender text NOT NULL,
  job_address text NOT NULL,
  job_lat double precision,
  job_lng double precision,
  move_in_date date NOT NULL,
  budget_min integer NOT NULL,
  budget_max integer NOT NULL,
  email text NOT NULL UNIQUE,
  phone text NOT NULL,
  pref_age_min integer DEFAULT 18,
  pref_age_max integer DEFAULT 99,
  pref_genders text[] DEFAULT '{}'::text[],
  pref_location_km integer DEFAULT 25,
  pet_allergy boolean DEFAULT false,
  sleep_time text,
  cleanliness integer,
  people_in_room integer,
  temperature_pref text,
  lease_duration text,
  cooking_habits text,
  smoking boolean,
  has_pet boolean,
  pet_preference text,
  interests text[] DEFAULT '{}'::text[],
  questionnaire_complete boolean DEFAULT false,
  CONSTRAINT users_pkey PRIMARY KEY (id)
);

CREATE TABLE public.connections (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  user_a uuid NOT NULL,
  user_b uuid NOT NULL,
  status text NOT NULL DEFAULT 'pending'::text,
  initiated_by uuid NOT NULL,
  created_at timestamp with time zone DEFAULT now(),
  updated_at timestamp with time zone DEFAULT now(),
  CONSTRAINT connections_pkey PRIMARY KEY (id),
  CONSTRAINT connections_user_a_fkey FOREIGN KEY (user_a) REFERENCES public.users(id),
  CONSTRAINT connections_user_b_fkey FOREIGN KEY (user_b) REFERENCES public.users(id),
  CONSTRAINT connections_initiated_by_fkey FOREIGN KEY (initiated_by) REFERENCES public.users(id)
);
